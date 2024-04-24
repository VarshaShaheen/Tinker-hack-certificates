from flask import Flask, render_template, jsonify, send_from_directory
import os

app = Flask(__name__)

venues = {
    'Adi_Shankara_Institute_of_Engineering_and_Technology': ['Binary_Trio', 'BugX', 'Cipher', 'Geekgals', 'Glitch',
                                                             'HackHers', 'Icetians', 'Mera', 'Sandbox_squad'],
    'Ahalia_School_of_Engineering_&_Technology': ['Anika', 'Bugsquashers', 'Morpho', 'Phoenix', 'WELKINS'],
    'Christ_College_of_Engineering_(CCE)': ['codebusters', 'CoderVerse', 'Data_pirates', 'DevDynamos', 'Distrackt',
                                            'Hipogriff', 'Mad_i³', 'Pixel', 'RARE', 'SheCodes', 'Team123', 'Triad',
                                            'Zephyr'],
    'COE_Munnar': ['#GAAA', 'Eureka', 'Idea_fusion', 'Jazzix', 'Makers', 'Newton', 'Sky', 'Strawhats', 'Syntax_Error'],
    'College_of_Engineering,_Chengannur': ['Azure', 'Binary_Brains', "Bits_N'_Bytes", 'Codex', 'Cosmo', 'Falcons',
                                           'Gryffindor', 'Jamu2.0', 'Jamu_1.0', 'Leviate', 'Md_Farhad', 'Nest', 'Orion',
                                           'Shana', 'TechSorority', 'THE_OGs'],
    'College_of_Engineering_and_Management_Punnapra': ['Bit_Belles', 'CodeX', 'Genesis', 'HerHack', 'Logicloom',
                                                       'Passioners', 'TechNexus', 'Tech_hack', 'Zeal'],
    'College_of_Engineering_Karunagappally': ['AI_BMCE', 'BellatorX', 'Byte_Guardians', 'Code_crusaders',
                                              'Computer_Crew', 'Cypher_Chicks', 'First-up', 'Initium_Novum',
                                              'Josna_J_John', 'Quad_Squad', 'Reloop', 'Screen_Warriors', 'She_tech',
                                              'Tech_trio', 'tonytony', 'Trio_Tech'],
    'College_of_Engineering_Pathanapuram': ['Event_Horizon', 'Hack_Heroes', 'Ignites', 'Immortals', 'Kriya',
                                            'Little_bits', 'Solvers', 'Star_Techies', 'Studious_Coders', 'Tech_Titans',
                                            'Tetrad', 'The_ECE'],
    'College_of_Engineering_Vadakara': ['111', 'Avengers', 'Codematez', 'Dotdotdot', 'Galazy', 'Gliders', 'Room117',
                                        'XYZ'],
    'GCE_KANNUR': ['405_Found', 'Binary', 'Blue_moon', 'Ergophile', 'Hack_typhoon', 'LadyGeeks', 'Philomath'],
    'GEC_Palakkad': ['Blaze_minds', 'Code_Commandos', 'Code_Crew', 'Hashtag', 'Hexcode', 'Innovista', 'Neophytes',
                     'Off-track', 'Pumpkins', 'Tech_Titan', 'Three_blitz'],
    'GEC_Thrissur': ['A_Sireesha_Menon', 'Binary_Belles', 'ByteCoders', 'Codecrafters', 'codecrew', 'Ctrl-Z_Squad',
                     'Electric_Eves', 'Enigma', 'Pink_Hackers', 'Virtual_replica', 'Wunderkinds'],
    'Jyothy_Engineering_College': ['Binary_brains', 'CrossBytes', 'GMG', 'Hackable', 'HackHerz', 'Hash_something_out.',
                                   'Innoplus', 'InnovationX', 'Innovators_next_gen', 'Miracle_tech', 'Pink_hackers',
                                   'REBOOT', 'Superscapes', 'Syntax_Squad', 'Tech_titans', 'The_deciders', 'ToDev'],
    'Kmea_College_Of_Engineering': ['Astros', 'Code_dreamers', 'Code_Queens', 'Dart', 'Error_404', 'FOUR_A',
                                    'HackCrack', 'Lunamovas', 'mbcians', 'Meta', 'Team_Aurora'],
    'LBS_College_of_Engineering_Kasaragod': ['AvengHERs', 'BETA', 'Gamma', 'Neotericz', 'Phishers', 'Team_alpha',
                                             'Team_Semicolon'],
    'LBS_Institute_of_Technology_for_Women_(LBSITW)': ['AccessNotDenied', 'Amethyst', 'Angel_Roy', 'Aurora',
                                                       'Avalanche', 'Bit_High', 'ByteBelles', 'Byte_Sync',
                                                       'Code_Zombies', 'Codisters', 'Crimson_Valor', 'DigitalDuo', 'Falcons', 'Hack_and_Codey', 'Hack_Wizards', 'Oculus', 'P4', 'Phoenix', 'Sapphire', 'Spark', 'SYAMINI_S', 'Team_Avenir', 'TechVoyagers', 'The_Minions', 'Titanium4', 'WhiteHats', 'Wicked_duo'],
    'Mar_Athanasius_College_of_Engineering': ['Allies', 'Auratecz', 'Code4hack', 'Codecrafters', 'Ctrl-Alt-Defeat', 'Curie', 'Error_404', 'Gryffindor',
    'HackHive', 'Hack_on_three', 'Hi-kons', 'Ideal_bits', 'Idea_Pioneers', 'MASALA_DOSA'],
    'Muthoot_Institute_of_Technology_and_Science_(MITS)': ['Athenians', 'Bits_n_Bytes', 'Code_Crew', "Code_crusher's",
                                                       'Crusaders', 'Ctrl_Alt_Del', 'Data-miners', 'Error_Hack',
                                                       'Firewall', 'HackSphere', 'Optimus_Prime', 'Probers', 'QuadNet',
                                                       'Radical_Skadattle', 'StyleBot', 'TechTitans', 'Tech_Army',
                                                       'Tech_Squad', 'Unity_hacks'],
    'NSSCE_Palakkad': ['Alchemists', 'Alpha_Code', 'AvengHERs', 'Bold_bytes', 'Codecrafters', 'Codehers', 'Dracarys',
                   'Ecoforecasters', 'Glitch_Grrrlz', 'Innov8Tech', 'Kodebreaker', 'Miracle', 'Off-track', 'One_N_Zero',
                   'Strikers', 'Technocrats', 'Techtitans', 'Vyuha'],
    'Rajagiri_School_of_Engineering_&_Technology': ['Binary_Coders', 'Bug_Strippers', 'CIUUDEVS', 'Code_Explorers',
                                                'CtrlAltElite', 'Error404', 'Hackasaurus_rex', 'hack_attackHers',
                                                'SheNinjas', 'TechSquad', 'TechTitans', 'Tech_Titans'],
    'RIT_Kottayam': ['Beginners', 'Code_Wizards', 'Coding_queens', 'Femhacks', 'PixelNinjas', 'Sensei', 'SIGS', 'SKS',
                 'Software_Chasers', 'SPAJ'],
    'Saintgits_College_of_Engineering': ['Bytes', 'Codex', 'Code_Catalysts', 'Data_Pirates', 'Dual_sync', 'Ideal_bits',
                                     'J.A.S', 'Pixels', 'Pixies', 'Striders', 'Strivers'],
    'SCMS_School_of_Engineering_&_Technology': ['Ampersand', 'Apricodes', 'Bitsnbytes', 'CODE_CRAFTERS', 'Columbus',
                                            'Ctrl_guards', 'Genecode', 'Iamironman', 'InnovateHers', 'Klan', 'Mystrex',
                                            'Ones_and_zeros', 'Phoenix', 'phoenix_flames', 'Retro_Coders',
                                            'Serendipity', 'Sparkle_Tech', 'TechySaavy', 'Tech_ti', 'Tech_titans',
                                            'Wistell'],
    'Sullamussalam_College_Areacode': ['HackHerHive', 'Hercode_crew', 'Scorpio', 'VshowedUp'],
    'Tinkerspace': ['Binary_Coders', 'BUG', 'byte_buster', 'CodeCrafters', 'CodeCrushers', 'CODE_RED', 'CODE_VIOLET',
                'Fe-Code', 'Little_Bits', 'Live', 'PraxisUS', 'Preyaswi_v_v', 'Shecoder', 'Spectre', 'Team',
                'Trojan_horse', 'We_3'],
    'TKM_College_Of_Engineering': ['Afaadnima', 'Casmenta', 'CodeQueens', 'CodeTesters', 'CyberSisters', "Dev's_Code",
                               'Git_Bash', 'HAvoCK', 'HugsForBugs', 'Impactors', 'Strikers', 'TechButterflies',
                               'Techwow', 'Tech_Phantoms', 'Tech_Titans', 'Valkyrie'],
    'Vimal_Jyothi_Engineering_College': ['Aspires', 'Bit_Rebels', 'Gryffindor', 'Musketeers', 'Surabhi_girls', 'Vj4'],
    'Zil_Money': ['Binary_bossess', 'Blitz', 'EKCIANS', 'Gamma', 'HackHERS', 'Hackit', 'Hactivate', 'Hakers', 'Lumos',
              'Mission_impossible', 'Pixies', 'Pogues', 'Team_EKC', 'Tech_Blog', 'Tech_tycoons', 'UNICORN', 'Winners',
              'zenith'],
}

@app.route('/')
def index():
    return render_template('index.html', venues=venues.keys())


@app.route('/teams/<venue>')
def teams(venue):
    return jsonify(venues[venue])


@app.route('/download/<venue>/<team>')
def download(venue, team):
    directory = os.path.join('certificates', venue)  # Ensure this path exists and contains the zip files.
    filename = f'{team}.zip'
    return send_from_directory(directory, filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
