
from pirates import *
from Roles import SmartPirate, Roles, Carrier

class PirateGroup:
    def __init__(self, _id, _list):
        self.pirates = _list
        self.group_id = _id


    def add(self, spirate):
        self.pirates.append(spirate)
        #game.debug("f")


    def remove(self, pirate):
        self.pirates.remove(pirate)

    def merge(self, pgroup):
        for pirate in pgroup.pirates:
            pgroup.remove(pirate)
            self.add(pirate)
        self.id = min(self.group_id, pgroup.group_id)

    def regroup(self, dest):
        for pirate in self.pirates:
            pirate.add_dest(dest)

    def update(self):
        for pirate in self.pirates:
            pirate.update()

    def __str__(self):
        return str(self.pirates)



class PirateHandler:
    def __init__(self, game):
        self.groups = []
        self._game = game
        for pirate in game.get_all_my_pirates():
            group = PirateGroup(pirate.id, [])
            spirate = SmartPirate(pirate, self._game)
            group.add(spirate)
            self.groups.append(group)



    def assign_roles(self, game):
        pass

    def get_all_my_pirates(self):
        pirates = []
        for group in self.groups:
            pirates += group.pirates
        return pirates

    def update(self):
        for group in self.groups:
            # Remove dead groups
            if group.pirates == []:
                pass
            else:
                group.update()

    def get_pirate(self, id):
        for group in self.groups:
            for pirate in group.pirates:
                if pirate.id == id:
                    return pirate, group
        return None

    def get_workers(self, role):
        workers = []
        for pirate in self.get_all_my_pirates():
            if pirate.role is not None:
                if pirate.role.roleId == role:
                    workers.append(pirate)
        return workers

    def set_pirate_role(self, pId, role):
        pirate, group = self.get_pirate(pId)
        n_pirate = Roles[role]["_class"](pirate)
        group.remove(pirate)
        group.add(n_pirate)
        return n_pirate


    def debug(self, game):
        for group in self.groups:
            self._game.debug(str(group))



"""




                                                                                                                                                               ..`
                                                                                                                                                             .+#@@'
                                                                                                                                                           .#@#'''@
                                                                                                                                                         `+@+''''#.
                                                                                                                                                        ,@+''''''@
                                          .;+#@##+;.                                                                                                   +@'''''''':
                                      :##+;''''''';'##`                                                                                              ,##''''''''@
                                   ;#+;''''''''''''''''@                                                                                           ,+@'''''''''#+
                                 ;#;''''''''''''''''''''+'                                                                                       .+@#'''''''''##
                               `@'''''''''''''''''''''''';#                                                                                     '##''''''''''@:
                              ,+'''''''''''''''''''''''''';@                                                                                  `#@'''''''''''@`
                             :''''''''''''''''''''''''''''''#                                                                                :@#'''''''''''#
                             +''''''''';;;'''''''''''''''''''#                                                                              +#''''''''''''#`
                            @'''':''';;;;;;;''''''''''''''''''@                                                                           `#+'''''''''''''#
                           ;''''::;';;;;;;;;;''''''''''''''''''@                                                                         :#+''''''''''''''+@@@@@@@@@##
                           #''::::;';;;;#@##@#''''''''''''''''';#                                                                      :@@+''''''''''''''''''''''''''@
                          .;':::::';:#'`......`;#;''''''''''''''';                                                                   :@+''''''''''''''''''''''''''''+#
                          +''::::;'+'`....`.....`+'''''''''''''''+                                                                 `@+'''''''''''''''''''''''''''''#@
                          #''::::;@`..`;@+'+@#:`..+'''''''''''''''@                                                               .@'''''''''''''''''''''''''''''+#.
                         `''':::'#..`'';;;;;;;:'#'+''''''''''''''';+                                                              @''''''''''''''''''''''''''+#@@'
                         ,;'':::#..`#;;;;;;;;;;;;;;;'''''''''''''''+`                                                            #''''''''''''''''''''''''#@#+,
                         +'''::@`.:';;;;;;;;;;;;;;;;;'''''''''''''''@                                                           :#''''''''''''''''''''''##',
                         #''''';.:;;;;;;;;;;;;;;;;;;;'''''''''''''''':                                                         ;@''''''''''''''''''''#@#.
                         #'''''#':;;;;;;;;;;;;;;;;;;;;'''''''''''''''@                                                       `#+''''''''''''''''++#@+.
                         @'''''';;;;;;;;;;;;;;;;;;;;;;''''''''''''''';;                                                     +@''''''''''''''''#@+:`
                         @'''''';;;;;;;;;;;;;;;;+@#@':''''''''''''''''#                                                  `#@+''''''''''''''''@'
                         @''''';;;;;;;;;;;;;;;#, ``` ;'''''''''''''''';;                                               `##''''''''''''''''+@@.
                         #''''';;;;;;;;;;;;;;#`````````+'''''''''''''''#                                               @'''''''''''''''''@+.
                         #''''';;;;;+###;;;;# `````````;;'''''''''''''';:                                            `@''''''''''''''''##
                         @''''';;;#``````+;:,`````````` +'''''''''''''''@                                           +@'''''''''''''''+@:
                         @''''';'.````````;' ```````````#''''''''''''''';.                                        ,@+'''''''''''''''#+
                         #''''':,`````````#' ```````````;''''''''''''''''@                                       ##''''''''''''''''#,
                         #'''''@`````````` ' ````:'`````;;''''''''''''''''                                     '@'''''''''''''''''#;
                         '''''';```````````'.````:'`````+''''''''''''''''''                                  :@+''''''''''''''''''#
                         :;''''.```````````#@```````````+'''''''''''''''''#                                 '@'''''''''''''''''''+:
                         ,''''':``` :``````#;.`````````+;''''''''''''''''';.                              .##''''''''''''''''''''#`
                         `'''''@```:@``````+;# `````` #:;''''''''''''''''''@                            ,#@+'''''''''''''''''''''#
                          +''''' `````````,:;;+;   .++;;;+'''''''''''''''''+                        +@#@+'''''''''''''''''''''''@
                          #'''''#```````` #;;;;;;';:;;;;;+''''''''''''''''';;                    ,:@@#'''''''''''''''''''''''''#,
                          @''''';'`````` #';;;;;;;;;;;:#;;''''''''''''''''''@           ,'#@++++++#+@+''''''''''''''''''''''''#+
                          @'''''':@.```'':;;;;';;;;+++:;;'@+'''''''''''''''''        :#@+'''''''''''+#@''''''''''''''@'''''''#'
                          ''''''';;:;;;;;;+;;;';;;;;;;;:;;;;;@;''''''''''''';;    ;@#+''''''''''''''''+##''''''''''''#''''''#:
                          .;''''';#;;;;;+;#;;;;;;;;;;#+###@';;+''''''''''''''@`;##''''''''''''''''''''''+#'''''''''''#'''''+:
                           ''''''';##+##;;#;;';;;;:@;,'#####@;;#'''''''''''''+#+''''''''''''''''''''''''''@''''''''''++''';;
                           #'''''';;:;;;;;:;;#;;;;;,#@#######@;:+'''''''''''';+''''''''''''''''''''''''''''#'''''''''++'''#
                           #''''';@+:;;;;;;+@';;'#,,##########;;#'''''''''''''@''''''''''''''''''''''''''''#'''''''''#'''@
                           #'''''';;'';;;;;;;;;+,,############+;''''''''''''''@'''''''''''''''''''''''''''''#'''''''''''#`
                           ;;'''+;##,,#'@';;;;##..#############;;'''''''''''''#'''''''''''''''''''''''''''''@''''''''''#.
                           .;''@;###.:#,,'.,,,,################;;''''''''''''''+'''''''''''''''''''''''''''''#'''''''+@.
                            +''+;###+#+:,#:,'#;######;';;;+###;;'''''''''''''''@'''''''''''''''''''''''''''''#''''''#;
                            @'':'##########+#######;''';''';@@;;#''''''''''''''@'''''''''''''''''''''''''''''@'''+@;`
                            #'';'##################;+@###'''';;:+''''''''''''''@'''''''''''''''''''''''''''''@';#:
                            ;;'+;########################:''';;@'''''''''''''''@'''''''''''''''''''''''''''''@+,
                            `''@;@#######################,:';;#;'''''''''''''''#'''''''''''''''''''''''''''''#
                             +'';:####################,,.';;;@'''''''''''''''''#''''''''''''''''''''''''''''';
                             #''#;;########+####,##,,@.:+:;;#''''''''''''''''''#''''''''''''''''''''''''''''#
                             #'''@;:@##+++,+#,.#,,@,,+':;;;;;''''''''''''''''''#'''''''''''''''''''''''''''+:
                             ;;'''@:;'@:,#,.+,,#;+#':;;;;;;;;''''''''''''''''''#''''''''''''''''''''''''''+'
                              '''''++:;;:;+''':;;;;;;;;;;;;;;''''''''''''''''''#'''''''''''''''''''''''''++
                              #'''''''##';;:;;;;;;;;;;;;;;;;;''''''''''''''''''#'''''''''''''''''''''''''+
                              @''''''';;;:;;;;;;;;;;;;;;;;;;;''''''''''''''''''#'''''''''''''''''''''''+#
                              ;'''''''';;;;;;;;;;;;;;;;;;;;;;''''''''''''''''''#'''''''''''''''''''''#@,
                              `;'''''''';;;;;;;;;;;;;;;;;;;;;''''''''''''''''''+'''''''''''''''''''@;
                               +'';''''';;;;;;;;;;;;;;;;;;;;;''''''''''''''''''+'''''''''''''''''''+
                               @';''''''';;;;;;;;;;;;;;;;;;;;''''''''''''''''''+''''''''''''''''''+.
                               +';''''''';;;;;;;;;;;;;;;;;;;;''''''''''''''''''@''''''''''''''''''#
                               ,';'''''''';;;;;;;;;;;;;;;;;;;;'''''''''''''''''@'''''''''''''''''#`
                                +;++''''''';;;;;;;;;;;;;;;;;;;'''''''''''''''''@''''''''''''''''+:
                                @':';'''''';;;;;;;;;;;;;;;;;;;'''''''''''''''''#''''''''''''''''+
                                +'';''''''';;;;;;;;;;;;;;;;;;;''''''''''''''''''''''''''''''''''+
                                ,;'''''''''';;;;;;;;;;;;;;;;;;''''''''''''''''+'''''''''''''''''+
                                :''''''''''';;;;;;;;;;;;;;;;;;''''''''''''''''#'''''''''''''''''+
                               `##'''''''''';;;;;;;;;;;;;;;;;;''''''''''''''''@'''''''''''''''''+
                              :#'#''''''''''';;;;;;;;;;;;;;;;;''''''''''''''''@'''''''''''''''''#
                            .@+''@''''''''''';;;;;;;;;;;;;;;;;''''''''''''''''@'''''''''''''''''@
                          `##'''''+'''''''''';;;;;;;;;;;;;;;;;''''''''''''''''@''''''''''''''''+'
                         ,@'''''''#'''''''''';;;;;;;;;;;;;;;;;''''''''''''''''#''''''''''''''''@`
                        `@''''''''''''''''''';;;;;;;;;;;;;;;;;;'''''''''''''''+''''''''''''''''@
                       `@'''''''''''''''''''';;;;;;;;;;;;;;;;;;:'''''''''''''#'''''''''''''''''#
                       ++''''''''''@'''''''''';;;;;;;;;;;;;;;;;''''''''''''''@'''''''''''''''''+
                      ,@'''''''''''#'''''''''';;;;;;;;;;;;;;;;;''''''''''''''+''''''''''''''''+;
                      #'''''''''''''#''''''''';;;;;;;;;;;;;;;;;'''''''''''''@'''''''''''''''''+`
                     ;+'''''''''''''#'''''''''';;;;;;;;;;;;;;;;''''''''''''@''''''''''''''''''+:
                     @'''''''''''''''@'''''''''';;;;;;;;;;;;;;'''''''''''+@'''''''''''''''''''+'
                    ''''''''''''''''''@''''''''';;;;;;;;;;;;;;''''''''''@+''''''''''''''''''''+'
                   .#''''''''''''''''''##''''''';;;;;;;;;;;;;;''''''''#@'''''''''''''''''+++++'@
                   @'''''''''''''''''''''@@'''''';;;;;;;;;;;'''''''+@@'''''''''''''''#@##+++''@#`
                  '+'''''''''''''''''''''''+@@+''';;;;;;;'''+#@+@#+'''''''''+###@@@##''''''''''#;
                 .#''''''''''''''''''''''''''''+#@@@@@@@@@@+'''''''''''''#@@+'''''''''''''''''#+#
                 #'''''''''''''''''''''''''''''''''''''''''''''''''''++@#+'''''##@@@@@@@@@@@@#''@
                .#++++''''''''''''''''''''''''''''''''''''''''''''#@##'''''''''+'''''''''''''@''#
                @+++++#@+''''''''''''''''''''''''''''''''''''''#@#''''''''''''''''''''''''''''@'#
               ,#'''''''+#@+''''''''''''''''''''''''''''''''+@#'''''''''''''''##@######'#######'+
               @''''''''''''#@#'''''''''''''''''''''''''''+@+'''''''''''''''''''''''''@@+'''''''+
              :+''''''''''''''+##'''''''''''''''''''''''#@#''''''''''''''''''''''''''+@'''''''''+
             `@'''''''''''''''''+#''''''''''''''++++##@#'''''''''''''''''''''''''+#@@+''''''''''+`
             @'''''''''''''''''''+#++'''''++@@##+++''''''''''''''''''''''''''''#@#''''''''''''''+.
            #+'''''''++#@@@@@@+''''++######+'''''''''''''''''''''''''''''''+#@+'''''''''''''''''+;
           +#'''+#@@#++''''''''''''''''''''''''''''''''''''''''''''''''''''+#'''''''''''''''''''+;
          ;#''#@#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''##''''''''''''''''''''+:
         +@'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''+@+'''''''''''''''''''''+:
        ,@'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''##'''''''''''''''''''''''+:
       `@''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#@'''''''''''''''''''''''''+;
       +#''''''''''''''''''''''''''''''''''''''''''''''''''''''+##@@#''''''''''''''''''''''''''''+
       @''''''''''''''''''''''''''''''''''''''''''''''+##@@@@@#+'''''''''''''''''''''''''''''''''#
      ;#''''''''''''''''''''''''''''''''''''''''###@@#+++''''''''''''''''''''''''''''''''''''''''@
      #'''''''''''''''''''''''''''''''''''''''##+''''''''''''''''''''''''''''''''''''''''''''''''@
      @'''''''''''''''''''''''''''''''''''''#@+''''''''''''''''''''''''''''''''''''''''''''''''''#`
      #''''''''''''''''''''''''''''''''''+@#'''''''''''''''''''''''''''''''''''''''''''''''''''''#.
      ++'''''''''''''''''''''''''''''''@@+'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
       @''''''''''''''''''''''''''''+@#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
       ++'''''''''''''''''''''''''+@#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
        @'''''''''''''''''''''''#@+'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''@
        .#''''''''''''''''''''#@;+''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
         '+''''''''''''''''+@+`  #''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
          +#'''''''''''''+@,     #''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
           ;@+'''''''''+@+       :+'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
             ;+###';;;;:          #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''@
                                  #''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''+,
                                  .+'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
                                   @'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''@
                                   #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''@
                                   :+''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#.
                                   .@'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#.
                                    @'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#'
                                    #''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#:
                                    '#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#'`
                                    ;@''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#;
                                    ,#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#'`
                                    ,@'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#:
                                    .#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#:

 """