import time

from owcv import ComputerVision


class OverwatchStateTracker:
    def __init__(self):
        coords = {
            "elimination": [749, 850, 832, 976],
            "assist": [749, 850, 832, 976],
            "save": [749, 850, 727, 922],
            "killcam": [89, 107, 41, 69],
            "death_spec": [66, 86, 1416, 1574],
            "being_beamed": [762, 807, 460, 508],
            "being_orbed": [857, 883, 172, 198],
            #"hacked": [858, 882, 171, 198], Old Version
            "hacked": [856, 884, 169, 199],
            "overtime": [37, 57, 903, 1016],
            #"baptiste_weapon": [962, 986, 1809, 1842],
            #"brigitte_weapon": [947, 985, 1695, 1773],
            #"kiriko_weapon": [952, 984, 1641, 1752],
            #"lucio_weapon": [942, 986, 1701, 1747],
            #"mercy_staff": [942, 981, 1666, 1747],
            #"mercy_pistol": [940, 980, 1666, 1726],
            "mercy_heal_beam": [672, 706, 807, 841],
            "mercy_damage_beam": [673, 705, 1080, 1112],
            "mercy_resurrect_cd": [920, 1000, 1570, 1655],
            #"zen_weapon": [942, 981, 1695, 1746],
            "zen_harmony": [954, 986, 738, 762],
            "zen_discord": [954, 985, 1157, 1182],

            #----------------CyberKitty's Addition
            ##WIDOWMAKER##
            #Widow Scoped
            "widow_isScoped_1":[732, 747, 929, 991],
            "widow_isScoped_2":[168, 211, 851, 1083],
            "widow_isScoped_3":[166, 189, 956, 1025],
            "widow_isScoped_4":[527, 555, 460, 517],
            "widow_isScoped_5":[727, 753, 922, 998],
            #Widow Ultimate
            "widow_is_Ulting":[525, 553, 104, 135],
            #Poison Bomb
            "widow_is_PoisonMine_active_1":[0, 1080, 0, 1920],
            "widow_is_PoisonMine_active_2":[0, 1080, 0, 1920] or [880, 911, 1570, 1600],
            "widow_is_PoisonMine_active_3":[859, 919, 1552, 1624],
            "widow_is_PoisonMine_active_4":[874, 919, 1558, 1613] or [871, 916, 1558, 1613] or [997, 1042, 1558, 1613],
            "widow_is_PoisonMine_active_5":[880, 911, 1570, 1600],
            #----------------CyberKitty's Addition
        }
        to_mask = [
        ]
        self.owcv = ComputerVision(coords, to_mask)
        self.current_time = 0
        self.hero = "Other"
        self.detected_hero = "Other"
        self.detected_hero_time = 0
        #self.hero_auto_detect = True
        self.in_killcam = False
        self.death_spectating = False
        self.is_dead = False
        self.notifs = []
        self.total_new_notifs = 0
        self.new_eliminations = 0
        self.new_assists = 0
        self.new_saves = 0
        self.being_beamed = False
        self.being_orbed = False
        self.hacked = False

        # Mercy-specific attributes
        self.mercy_heal_beam = False
        self.mercy_damage_beam = False
        self.mercy_resurrecting = False
        self.mercy_heal_beam_buffer = 0
        self.mercy_damage_beam_buffer = 0
        self.mercy_beam_disconnect_buffer_size = 8

        # Zenyatta-specific attributes
        self.zen_harmony_orb = False
        self.zen_discord_orb = False
        self.zen_harmony_orb_buffer = 0
        self.zen_discord_orb_buffer = 0
        # Orbs take up to 0.8s to switch targets at max range (w/ ~40ms RTT)
        self.zen_orb_disconnect_buffer_size = 30

        #----------------CyberKitty's Addition
        #-----------WIDOWMAKER-----------#
        #Widow Scoped detection 1
        self.widow_is_Scoped_1 = False
        self.widow_isScoped_disconnect_buffer_size_1 = 15
        self.widow_is_Scoped_buffer_1 = 0
        #Backend Widow Scoped Alternate Detection 2
        self.widow_is_Scoped_2 = False
        self.widow_isScoped_disconnect_buffer_size_2 = 15
        self.widow_is_Scoped_buffer_2 = 0
        #Backend Widow Scoped Alternate Detection 3
        self.widow_is_Scoped_3 = False
        self.widow_isScoped_disconnect_buffer_size_3 = 15
        self.widow_is_Scoped_buffer_3 = 0
        #Backend Widow Scoped Alternate Detection 4
        self.widow_is_Scoped_4 = False
        self.widow_isScoped_disconnect_buffer_size_4 = 15
        self.widow_is_Scoped_buffer_4 = 0
        #Backend Widow Scoped Alternate Detection 5
        self.widow_is_Scoped_5 = False
        self.widow_isScoped_disconnect_buffer_size_5 = 15
        self.widow_is_Scoped_buffer_5 = 0

        
        #Widowmaker Ultimate
        self.widow_is_Ulting = False
        
        #TODO:Widow Poison Mine
        self.widow_is_PoisonMine_active_1 = False
        self.widow_is_PoisonMine_active_disconnect_buffer_size_1 = 15
        self.widow_is_PoisonMine_active_buffer_1 = 0
        self.widow_is_PoisonMine_active_2 = False
        self.widow_is_PoisonMine_active_disconnect_buffer_size_2 = 15
        self.widow_is_PoisonMine_active_buffer_2 = 0
        self.widow_is_PoisonMine_active_3 = False
        self.widow_is_PoisonMine_active_disconnect_buffer_size_3 = 15
        self.widow_is_PoisonMine_active_buffer_3 = 0
        self.widow_is_PoisonMine_active_4 = False
        self.widow_is_PoisonMine_active_disconnect_buffer_size_4 = 15
        self.widow_is_PoisonMine_active_buffer_4 = 0
        self.widow_is_PoisonMine_active_5 = False
        self.widow_is_PoisonMine_active_disconnect_buffer_size_5 = 15
        self.widow_is_PoisonMine_active_buffer_5 = 0
        #----------------CyberKitty's Addition

    def refresh(self, capture_frame_only=False):
        self.owcv.capture_frame()
        if capture_frame_only:
            return

        # TODO: Shouldn't check for things that aren't enabled in the config
        self.current_time = time.time()
        self.expire_notifs()

        self.total_new_notifs = 0
        self.new_eliminations = 0
        self.new_assists = 0
        self.new_saves = 0

        # TODO: Find out if the player is alive (there is a period of time between death and killcam, should handle that with "you were eliminated" message and a timer)
        self.in_killcam = self.owcv.detect_single("killcam")
        if not self.in_killcam:
            self.death_spectating = self.owcv.detect_single("death_spec")
        player_is_alive = not (self.in_killcam or self.death_spectating)

        if player_is_alive:
            if self.is_dead:
                self.is_dead = False

            self.new_eliminations = self.detect_new_notifs("elimination")

            self.new_assists = self.detect_new_notifs("assist")

            self.new_saves = self.detect_new_notifs("save")

            self.being_beamed = self.owcv.detect_single("being_beamed")

            self.being_orbed = self.owcv.detect_single("being_orbed")

            self.hacked = self.owcv.detect_single("hacked")

            #----------------CyberKitty's Addition
            #-----------WIDOWMAKER-----------#
            self.widow_is_Scoped_1 = self.owcv.detect_single("widow_isScoped_1")#Changed Function to the 0.8 Threshhold version in to hopefully improove detection 1
            self.widow_is_Scoped_2 = self.owcv.detect_single("widow_isScoped_2")
            self.widow_is_Scoped_3 = self.owcv.detect_single("widow_isScoped_3")
            self.widow_is_Scoped_4 = self.owcv.detect_single("widow_isScoped_4")
            self.widow_is_Scoped_5 = self.owcv.detect_single("widow_isScoped_5")
            self.widow_is_Ulting = self.owcv.detect_single("widow_is_Ulting")
            self.widow_is_PoisonMine_active_1 = self.owcv.detect_single("widow_is_PoisonMine_active_1")
            self.widow_is_PoisonMine_active_2 = self.owcv.detect_single("widow_is_PoisonMine_active_2")
            self.widow_is_PoisonMine_active_3 = self.owcv.detect_single("widow_is_PoisonMine_active_3")
            self.widow_is_PoisonMine_active_4 = self.owcv.detect_single("widow_is_PoisonMine_active_4")
            self.widow_is_PoisonMine_active_5 = self.owcv.detect_single("widow_is_PoisonMine_active_5")
            #----------------CyberKitty's Addition

            if self.hero == "Mercy":
                self.detect_mercy_beams()

                if self.count_notifs_of_type("save") > 0:
                    self.mercy_resurrecting = self.owcv.detect_single("mercy_resurrect_cd")

            elif self.hero == "Zenyatta":
                self.detect_zen_orbs()

            #----------------CyberKitty's Addition
            elif self.hero == "Widowmaker":
                self.detect_widowUlt()
                self.detect_widowScope_1()
                self.detect_widowScope_2()
                self.detect_widowScope_3()
                self.detect_widowScope_4()
                self.detect_widowScope_5()
                self.detect_widow_PoisonMine_active_1()
                self.detect_widow_PoisonMine_active_2()
                self.detect_widow_PoisonMine_active_3()
                self.detect_widow_PoisonMine_active_4()
                self.detect_widow_PoisonMine_active_5()
                #TODO: Add detection for poison mine once created.
            #----------------CyberKitty's Addition

            # Detect hero swaps for 0.1 second every 3 seconds
            current_second = self.current_time - int(self.current_time / 10) * 10
            # if self.hero_auto_detect and int(current_second) % 3 == 0 and current_second % 1 < 0.1:
            #     self.detect_hero()

        # If player is dead:
        else:
            if not self.is_dead:
                self.is_dead = True
                self.being_beamed = False
                self.being_orbed = False
                self.hacked = False
                # Add a way to remove this duplication of code (repeats in switch_hero).
                # Probably, each hero should be a class and should have a method to zero its attributes. Instances could saved as self.mercy, self.zenyatta, etc. Or just as self.current_hero.
                if self.hero == "Mercy":
                    self.mercy_heal_beam = False
                    self.mercy_damage_beam = False
                    self.mercy_resurrecting = False
                    self.mercy_heal_beam_buffer = 0
                    self.mercy_damage_beam_buffer = 0
                elif self.hero == "Zenyatta":
                    self.zen_harmony_orb = False
                    self.zen_discord_orb = False
                    self.zen_harmony_orb_buffer = 0
                    self.zen_discord_orb_buffer = 0
                #----------------CyberKitty's Addition
                elif self.hero == "Widowmaker":
                    self.widow_is_Scoped_1 = False
                    self.widow_is_Ulting = False
                    self.widow_is_Scoped_2 = False
                    self.widow_is_Scoped_3 = False
                    self.widow_is_Scoped_4 = False
                    self.widow_is_Scoped_5 = False
                    self.widow_is_PoisonMine_active_1 = False
                    self.widow_is_PoisonMine_active_2 = False
                    self.widow_is_PoisonMine_active_3 = False
                    self.widow_is_PoisonMine_active_4 = False
                    self.widow_is_PoisonMine_active_5 = False
                    
                #----------------CyberKitty's Addition
#TODO:Make Sure To Add Widowmakers Gun Detection Here
    # def detect_hero(self):
    #     hero_detected = False
    #     heroes = {
    #         "zen_weapon": "Zenyatta",
    #         "mercy_staff": "Mercy",
    #         "mercy_pistol": "Mercy",
    #         "baptiste_weapon": "Baptiste",
    #         "brigitte_weapon": "Brigitte",
    #         "kiriko_weapon": "Kiriko",
    #         "lucio_weapon": "Lucio",
    #     }
    #     for hero_weapon, hero_name in heroes.items():
    #         if self.owcv.detect_single(hero_weapon, threshold=0.97):
    #             self.detected_hero = hero_name
    #             self.detected_hero_time = self.current_time
    #             hero_detected = True
    #             break
    #     # If no supported hero has been detected within the last 8 seconds:
    #     if not hero_detected and self.detected_hero != "Other" and self.current_time > self.detected_hero_time + 8:
    #         self.detected_hero = "Other"

    def switch_hero(self, hero_name):
        if self.hero == "Mercy":
            self.mercy_heal_beam = False
            self.mercy_damage_beam = False
            self.mercy_resurrecting = False
            self.mercy_heal_beam_buffer = 0
            self.mercy_damage_beam_buffer = 0
        elif self.hero == "Zenyatta":
            self.zen_harmony_orb = False
            self.zen_discord_orb = False
            self.zen_harmony_orb_buffer = 0
            self.zen_discord_orb_buffer = 0
        #----------------CyberKitty's Addition
        elif self.hero == "Widowmaker":
            self.widow_is_Scoped_1 = False
            self.widow_is_Scoped_2 = False
            self.widow_is_Scoped_3 = False
            self.widow_is_Scoped_4 = False
            self.widow_is_Scoped_5 = False
            self.widow_is_Ulting = False
            self.widow_is_PoisonMine_active_1 = False
            self.widow_is_Scoped_buffer_1 = 0
            self.widow_is_Scoped_buffer_2 = 0
            self.widow_is_Scoped_buffer_3 = 0
            self.widow_is_Scoped_buffer_4 = 0
            self.widow_is_Scoped_buffer_5 = 0
            self.widow_Ult_buffer = 0
            self.widow_is_PoisonMine_active_buffer_1 = 0
            self.widow_is_PoisonMine_active_buffer_2 = 0
            self.widow_is_PoisonMine_active_buffer_3 = 0
            self.widow_is_PoisonMine_active_buffer_4 = 0
            self.widow_is_PoisonMine_active_buffer_5 = 0
        #----------------CyberKitty's Addition
        self.hero = hero_name
        #----------------CyberKitty's Addition !!!--!!! MAY NOT NEED THIS !!!--!!!
        if self.hero != "Widowmaker":
            self.widow_scoped_vibe_active = False
            self.widow_is_Scoped_1 = False
            self.widow_is_Scoped_2 = False
            self.widow_is_Scoped_3 = False
            self.widow_is_Scoped_4 = False
            self.widow_is_Scoped_5 = False
            self.widow_is_Ulting = False
            self.widow_is_PoisonMine_active_1 = False
            self.widow_is_PoisonMine_active_2 = False
            self.widow_is_PoisonMine_active_3 = False
            self.widow_is_PoisonMine_active_4 = False
            self.widow_is_PoisonMine_active_5 = False
        #----------------CyberKitty's Addition !!!--!!! MAY NOT NEED THIS !!!--!!!
        

    def detect_new_notifs(self, notif_type):
        if self.total_new_notifs >= 3:
            return 0
        notifs_detected = self.owcv.detect_multiple(notif_type)
        existing_notifs = self.count_notifs_of_type(notif_type)
        new_notifs = max(0, notifs_detected - existing_notifs)
        for _ in range(new_notifs):
            self.add_notif(notif_type)
        self.total_new_notifs += new_notifs
        return new_notifs

    def count_notifs_of_type(self, notif_type):
        return sum(notif[0] == notif_type for notif in self.notifs)

    def get_expired_items(self, array, expiry_index):
        expired_items = []
        for item in array:
            if item[expiry_index] <= self.current_time:
                expired_items.append(item)
            else:
                break
        return expired_items

    def expire_notifs(self):
        for expired_notif in self.get_expired_items(self.notifs, 1):
            self.notifs.remove(expired_notif)

    def add_notif(self, notif_type):
        if len(self.notifs) == 3:
            del self.notifs[0]
        self.notifs.append([notif_type, self.current_time + 2.705])

    def detect_mercy_beams(self):
        if self.owcv.detect_single("mercy_heal_beam"):
            self.mercy_heal_beam_buffer = 0
            self.mercy_heal_beam = True
            self.mercy_damage_beam = False
            self.mercy_damage_beam_buffer = 0
        elif self.mercy_heal_beam:
            self.mercy_heal_beam_buffer += 1
            if self.mercy_heal_beam_buffer == self.mercy_beam_disconnect_buffer_size:
                self.mercy_heal_beam = False

        if self.owcv.detect_single("mercy_damage_beam"):
            self.mercy_damage_beam_buffer = 0
            self.mercy_damage_beam = True
            self.mercy_heal_beam = False
            self.mercy_heal_beam_buffer = 0
        elif self.mercy_damage_beam:
            self.mercy_damage_beam_buffer += 1
            if self.mercy_damage_beam_buffer == self.mercy_beam_disconnect_buffer_size:
                self.mercy_damage_beam = False

    def detect_zen_orbs(self):
        if self.owcv.detect_single("zen_harmony"):
            self.zen_harmony_orb_buffer = 0
            self.zen_harmony_orb = True
        elif self.zen_harmony_orb:
            self.zen_harmony_orb_buffer += 1
            if self.zen_harmony_orb_buffer == self.zen_orb_disconnect_buffer_size:
                self.zen_harmony_orb = False

        if self.owcv.detect_single("zen_discord"):
            self.zen_discord_orb_buffer = 0
            self.zen_discord_orb = True
        elif self.zen_discord_orb:
            self.zen_discord_orb_buffer += 1
            if self.zen_discord_orb_buffer == self.zen_orb_disconnect_buffer_size:
                self.zen_discord_orb = False

    #----------------CyberKitty's Addition          
    #-----------WIDOWMAKER-----------#
    def detect_widowScope_1(self):
        if self.owcv.detect_single("widow_isScoped_1", 0.7) and self.owcv: #Change to detect_singlelow if you want it to lock at threshold 8 instead of 9 (default) - Used in case the buffer isn't enough.
            self.widow_is_Scoped_buffer_1 = 0
            if not self.widow_is_Scoped_1:
                self.widow_is_Scoped_1 = True
        else:
            if self.widow_is_Scoped_1:
                self.widow_is_Scoped_buffer_1 -= 1
                if self.widow_is_Scoped_buffer_1 == -self.widow_isScoped_disconnect_buffer_size_1:
                    self.widow_is_Scoped_1 = False

    def detect_widowScope_2(self):# Second Backup Detection
        if self.owcv.detect_single("widow_isScoped_2", 0.8): 
            self.widow_is_Scoped_buffer_2 = 0
            if not self.widow_is_Scoped_2:
                self.widow_is_Scoped_2 = True
        else:
            if self.widow_is_Scoped_2:
                self.widow_is_Scoped_buffer_2 -= 1
                if self.widow_is_Scoped_buffer_2 == -self.widow_isScoped_disconnect_buffer_size_2:
                    self.widow_is_Scoped_2 = False
                    
    def detect_widowScope_3(self):# Third Backup Detection
        if self.owcv.detect_single("widow_isScoped_3", 0.8):
            self.widow_is_Scoped_buffer_3 = 0
            if not self.widow_is_Scoped_3:
                self.widow_is_Scoped_3 = True
        else:
            if self.widow_is_Scoped_3:
                self.widow_is_Scoped_buffer_3 -= 1
                if self.widow_is_Scoped_buffer_3 == -self.widow_isScoped_disconnect_buffer_size_3:
                    self.widow_is_Scoped_3 = False
                    
    def detect_widowScope_4(self):# Fourth Backup Detection
        if self.owcv.detect_single("widow_isScoped_4", 0.8):
            self.widow_is_Scoped_buffer_4 = 0
            if not self.widow_is_Scoped_4:
                self.widow_is_Scoped_4 = True
        else:
            if self.widow_is_Scoped_4:
                self.widow_is_Scoped_buffer_4 -= 1
                if self.widow_is_Scoped_buffer_4 == -self.widow_isScoped_disconnect_buffer_size_4:
                    self.widow_is_Scoped_4 = False
                    
    def detect_widowScope_5(self):# Fifth Backup Detection
        if self.owcv.detect_single("widow_isScoped_5", 0.8):
            self.widow_is_Scoped_buffer_5 = 0
            if not self.widow_is_Scoped_5:
                self.widow_is_Scoped_5 = True
        else:
            if self.widow_is_Scoped_5:
                self.widow_is_Scoped_buffer_5 -= 1
                if self.widow_is_Scoped_buffer_5 == -self.widow_isScoped_disconnect_buffer_size_5:
                    self.widow_is_Scoped_5 = False
                    
    def detect_widowUlt(self):
        if self.owcv.detect_single("widow_is_Ulting"): #Change to detect_singlelow if you want it to lock at threshold 8 instead of 9 (default) - Used in case the buffer isn't enough.
            self.widow_Ult_buffer = 0
            if not self.widow_is_Ulting:
                self.widow_is_Ulting = True
        else:
            if self.widow_is_Ulting:
                self.widow_Ult_buffer -= 1
                if self.widow_Ult_buffer == -self.widow_ult_disconnect_buffer_size:
                    self.widow_is_Ulting = False
                    #TODO: Finish Detection Function Below
    def detect_widow_PoisonMine_active_1(self):
        if self.owcv.detect_single("widow_is_PoisonMine_active_1", 0.8):
            self.widow_is_PoisonMine_active_buffer_1 = 0
            if not self.widow_is_PoisonMine_active_1:
                self.widow_is_PoisonMine_active_1 = True  
        else:
            if self.widow_is_PoisonMine_active_1:
                self.widow_is_PoisonMine_active_buffer_1 -= 1
                if self.widow_is_PoisonMine_active_buffer_1 == -self.widow_is_PoisonMine_active_disconnect_buffer_size_1:
                    self.widow_is_PoisonMine_active_1 = False
                    
    def detect_widow_PoisonMine_active_2(self):
        if self.owcv.detect_single("widow_is_PoisonMine_active_2", 0.8):
            self.widow_is_PoisonMine_active_buffer_2 = 0
            if not self.widow_is_PoisonMine_active_2:
                self.widow_is_PoisonMine_active_2 = True  
        else:
            if self.widow_is_PoisonMine_active_1:
                self.widow_is_PoisonMine_active_buffer_2 -= 1
                if self.widow_is_PoisonMine_active_buffer_2 == -self.widow_is_PoisonMine_active_disconnect_buffer_size_2:
                    self.widow_is_PoisonMine_active_2 = False
                    
    def detect_widow_PoisonMine_active_3(self):
        if self.owcv.detect_single("widow_is_PoisonMine_active_3", 0.8):
            self.widow_is_PoisonMine_active_buffer_3 = 0
            if not self.widow_is_PoisonMine_active_3:
                self.widow_is_PoisonMine_active_3 = True  
        else:
            if self.widow_is_PoisonMine_active_3:
                self.widow_is_PoisonMine_active_buffer_3 -= 1
                if self.widow_is_PoisonMine_active_buffer_3 == -self.widow_is_PoisonMine_active_disconnect_buffer_size_3:
                    self.widow_is_PoisonMine_active_3 = False
                    
    def detect_widow_PoisonMine_active_4(self):
        if self.owcv.detect_single("widow_is_PoisonMine_active_4", 0.8):
            self.widow_is_PoisonMine_active_buffer_4 = 0
            if not self.widow_is_PoisonMine_active_4:
                self.widow_is_PoisonMine_active_4 = True  
        else:
            if self.widow_is_PoisonMine_active_4:
                self.widow_is_PoisonMine_active_buffer_4 -= 1
                if self.widow_is_PoisonMine_active_buffer_4 == -self.widow_is_PoisonMine_active_disconnect_buffer_size_4:
                    self.widow_is_PoisonMine_active_4 = False
                    
    def detect_widow_PoisonMine_active_5(self):
        if self.owcv.detect_single("widow_is_PoisonMine_active_5", 0.8):
            self.widow_is_PoisonMine_active_buffer_5 = 0
            if not self.widow_is_PoisonMine_active_5:
                self.widow_is_PoisonMine_active_5 = True  
        else:
            if self.widow_is_PoisonMine_active_5:
                self.widow_is_PoisonMine_active_buffer_5 -= 1
                if self.widow_is_PoisonMine_active_buffer_5 == -self.widow_is_PoisonMine_active_disconnect_buffer_size_5:
                    self.widow_is_PoisonMine_active_5 = False
                    
    #-----------WIDOWMAKER-----------#
    #----------------CyberKitty's Addition

    def start_tracking(self, refresh_rate):
        self.owcv.start_capturing(refresh_rate)

    def stop_tracking(self):
        self.owcv.stop_capturing()
