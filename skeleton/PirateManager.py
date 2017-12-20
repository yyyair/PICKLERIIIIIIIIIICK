
from pirates import *

class SmartPirate:

    ERROR_PIRATE_NOT_IN_PUSH_RANGE = 1
    ERROR_PIRATE_PUSHED_TOO_FAR = 2
    ERROR_PUSH_COOLDOWN = 3

    def __init__(self, pirate, game):
        self._game = game
        self._pirate = pirate
        self.last_turn = -1
        self.waypoints = []

    # Attempts to move the pirate towards its current set destination
    def move(self):
        if len(self.waypoints)==0: return

        if self.last_turn != self._game.turn:
            self._pirate.sail(self.waypoints[-1])
            self.last_turn = self._game.turn
        if self._pirate.get_location() == (self.waypoints[-1]):
            self.remove_dest()

    # Adds a destination for the queue
    def add_dest(self, dest):
        self.waypoints.append(dest)

    # Removes the current destination from the queue
    def remove_dest(self):
        self.waypoints.remove(self.waypoints[-1])

    
    def push(self, target, dest):
        if self.last_turn != self._game.turn:
            if self._pirate.in_push_range(target):
                if target.distance(dest) > self._pirate.push_range:
                    if self._pirate.push_reload_turns == 0:
                        self._pirate.push(target, dest)
                        self.last_turn = self._game.turn

                else:
                    return SmartPirate.ERROR_PIRATE_PUSHED_TOO_FAR
            else:
                return SmartPirate.ERROR_PIRATE_NOT_IN_PUSH_RANGE



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

    def move(self):
        for pirate in self.pirates:
            pirate.move("sdf")

    def __str__(self):
        return str(self.pirates)



class PirateHandler:
    def __init__(self, game):
        self.groups = []
        self._game = game
        for pirate in game.get_all_my_pirates():
            group = None
            group = PirateGroup(pirate.id, [])
            self._game.debug(group.pirates)
            spirate = SmartPirate(pirate, self._game)
            group.add(spirate)
            self.groups.append(group)

    def assign_roles(self, game):
        pass

    def update(self, game):
        for group in self.groups:
            # Remove dead groups
            if group.pirates == []:
                pass

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