import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QTextEdit, QLabel, QScrollArea, QComboBox, QFrame, QCheckBox,
    QFileDialog, QRadioButton, QGridLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
import random
import numpy as np

WORLDLY_SETS = {
    "Japanese": list("あいうえおかきくけこさしすせそたちつてとなにぬねのまみむめもやゆよらりるれろわをんアイウエオカキクケコサシスセソタチツテトナニヌネノマミムメモヤユヨラリルレロワヲン"),
    "Korean": list("가나다라마바사아자차카타파하거너더러머버서어저처커터퍼허"),
    "Chinese": list("的一是不了人我在有他这中大来上国个到说们为子和你地出道也时年得就那要下以生会自着去之过家学对可里后小么心多天而能好都然没日于起还发成事只作当方"),
    "Russian": list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
    "Hindi": list("अआइईउऊएऐओऔकखगघचछजझटठडढतथदधनपफबभमयरलवशषसह"),
    "Aramaic": list("ܐܒܓܕܗܘܙܚܛܝܟܠܡܢܣܥܦܨܩܪܫܬ")
}

EMOJI_SET = [
    "😀","😃","😄","😁","😆","😅","😂","🤣","😊","😇","🙂","🙃","😉","😌","😍","🥰","😘","😗","😙","😚",
    "😋","😛","😜","🤪","😝","🤑","🤗","🤭","🤫","🤔","🤐","🤨","😐","😑","😶","😏","😒","🙄","😬","😮",
    "😯","😲","😳","🥺","😦","😧","😨","😰","😥","😢","😭","😱","😖","😣","😞","😓","😩","😫","🥱","😤",
    "😡","😠","🤬","😈","👿","💀","☠️","🤡","👹","👺","👻","👽","👾","🤖","🎃","😺","😸","😹","😻","😼",
    "😽","🙀","😿","😾","🐶","🐱","🐭","🐹","🐰","🦊","🐻","🐼","🐨","🐯","🦁","🐮","🐷","🐽","🐸","🐵",
    "🙈","🙉","🙊","🐒","🐔","🐧","🐦","🐤","🐣","🐥","🦆","🦅","🦉","🦇","🐺","🐗","🐴","🦄","🐝","🐛",
    "🦋","🐌","🐞","🐜","🪲","🪳","🪰","🪱","🐢","🐍","🦎","🦂","🦀","🦞","🦐","🐙","🦑","🪼","🐠","🐟",
    "🐡","🦈","🐬","🐳","🐋","🦭","🐊","🐆","🐅","🐃","🐂","🐄","🦬","🐪","🐫","🦒","🦓","🐘","🦣","🦏",
    "🦛","🐁","🐀","🐇","🦝","🦨","🦡","🐾","🐉","🐲","🌵","🎄","🌲","🌳","🌴","🌱","🌿","☘️","🍀","🎍",
    "🌾","🍁","🍂","🍃","🍇","🍈","🍉","🍊","🍋","🍌","🍍","🥭","🍎","🍏","🍐","🍑","🍒","🍓","🫐","🥝",
    "🍅","🍆","🥑","🥦","🥬","🥒","🌶️","🫑","🌽","🥕","🫒","🧄","🧅","🥔","🍠","🥐","🍞","🥖","🥨","🥯",
    "🧇","🥞","🧀","🍖","🍗","🥩","🥓","🍔","🍟","🍕","🌭","🥪","🌮","🌯","🥙","🧆","🥘","🍲","🍛","🍜",
    "🍝","🍠","🍢","🍣","🍤","🍥","🥮","🍡","🥟","🥠","🥡","🦪","🍦","🍧","🍨","🍩","🍪","🎂","🍰","🧁",
    "🥧","🍫","🍬","🍭","🍮","🍯","🍼","🥛","☕","🍵","🫖","🍶","🍺","🍻","🥂","🍷","🥃","🍸","🍹","🍾",
    "🧉","🧊","🥤","🧋","🍽️","🍴","🥄","🔪","🏺","🌍","🌎","🌏","🌐","🗺️","🗾","🏔️","⛰️","🌋","🗻","🏕️",
    "🏖️","🏜️","🏝️","🏞️","🏟️","🏛️","🏗️","🧱","🏘️","🏚️","🏠","🏡","🏢","🏣","🏤","🏥","🏦","🏨","🏩",
    "🏪","🏫","🏬","🏭","🏯","🏰","💒","🗼","🗽","⛪","🕌","🛕","🕍","⛩️","🕋","⛲","⛺","🌁","🌃","🏙️",
    "🌄","🌅","🌆","🌇","🌉","♨️","🎠","🎡","🎢","💈","🎪","🚂","🚃","🚄","🚅","🚆","🚇","🚈","🚉","🚊",
    "🚝","🚞","🚋","🚌","🚍","🚎","🚐","🚑","🚒","🚓","🚔","🚕","🚖","🚗","🚘","🚙","🚚","🚛","🚜","🛻",
    "🚲","🛴","🛵","🏍️","🚨","🚡","🚠","🚟","✈️","🛩️","🛫","🛬","🛸","🚀","🛶","⛵"
]

ZALGO_UP = [
    "̍","̎","̄","̅","̿","̑","̆","̐","͒","͗","͑","̇","̈","̊","͂","̓","̈","͊","͋","͌","̃","̂","̌","͐",
    "̀","́","̋","̏","̒","̓","̔","̽","̉","ͣ","ͤ","ͥ","ͦ","ͧ","ͨ","ͩ","ͪ","ͫ","ͬ","ͭ","ͮ","ͯ"
]

ZALGO_MID = [
    "̕","̛","̀","́","͘","̡","̢","̧","̨","̴","̵","̶","͜","͝","͞","͟","͠","͢","̸","̷"
]

ZALGO_DOWN = [
    "̖","̗","̘","̙","̜","̝","̞","̟","̠","̤","̥","̦","̩","̪","̫","̬","̭","̮","̯","̰","̱","̲","̳",
    "̹","̺","̻","̼","ͅ","͇","͈","͉","͍","͎","͓","͔","͕","͖","͙","͚","̣"
]

GLITCH_CHARS = [
    "▒","▓","░","█","▞","▚","▛","▜","▟","▙",
    "�","�","�","⌁","⌇","⌦","⌧","⍉","⍊","⍟",
    "⧖","⧗","⧘","⧙","⧚","⧛","⧜","⧝","⧞","⧟"
]

DIGITAL_NOISE = [
    "@","#","$","%","&","*","/","\\","=","+",
    "~","^","<",">","|","¬","§","¶","•","¤"
]

PUNC_EXPLOSIVE = ["!", "?", "!!", "???", "!?"]
PUNC_CHAOTIC = ["!?", "?!", ".!?", "!..?", "?!!", "!!?"]
PUNC_OVERLOAD = ["...", ".....", "~~~~", "!!!!!", "?????", "~~!!??"]
PUNC_ASCII = [
    "¯\\_(ツ)_/¯",
    "(╯°□°）╯︵ ┻━┻",
    "(ノಠ益ಠ)ノ彡┻━┻",
    "(ง'̀-'́)ง",
    "(•̀ᴗ•́)و",
    "(ᗒᗣᗕ)՞"
]

# Unicode fancy font maps
FANCY_MAPS = {
    "Cursive": ("𝒶","𝒷","𝒸","𝒹","𝑒","𝒻","𝑔","𝒽","𝒾","𝒿","𝓀","𝓁","𝓂","𝓃","𝑜","𝓅","𝓆","𝓇","𝓈","𝓉","𝓊","𝓋","𝓌","𝓍","𝓎","𝓏"),
    "Bold Mono": ("𝙖","𝙗","𝙘","𝙙","𝙚","𝙛","𝙜","𝙝","𝙞","𝙟","𝙠","𝙡","𝙢","𝙣","𝙤","𝙥","𝙦","𝙧","𝙨","𝙩","𝙪","𝙫","𝙬","𝙭","𝙮","𝙯"),
    "Fullwidth": ("ａ","ｂ","ｃ","ｄ","ｅ","ｆ","ｇ","ｈ","ｉ","ｊ","ｋ","ｌ","ｍ","ｎ","ｏ","ｐ","ｑ","ｒ","ｓ","ｔ","ｕ","ｖ","ｗ","ｘ","ｙ","ｚ"),
    "Script": ("𝓪","𝓫","𝓬","𝓭","𝓮","𝓯","𝓰","𝓱","𝓲","𝓳","𝓴","𝓵","𝓶","𝓷","𝓸","𝓹","𝓺","𝓻","𝓼","𝓽","𝓾","𝓿","𝔀","𝔁","𝔂","𝔃")
}

BLACKLETTER_MAP = (
    "𝔞","𝔟","𝔠","𝔡","𝔢","𝔣","𝔤","𝔥","𝔦","𝔧","𝔨","𝔩","𝔪","𝔫","𝔬","𝔭","𝔮","𝔯","𝔰","𝔱","𝔲","𝔳","𝔴","𝔵","𝔶","𝔷"
)

DRAMATIC_PHRASES = [
    "…in the shadows",
    "…as the world fades",
    "…lost in the void",
    "…where silence screams",
    "…beneath broken skies"
]

POETIC_SADNESS = [
    "softly aching",
    "quietly unraveling",
    "a whisper of sorrow",
    "fragile as dusk",
    "woven from longing"
]

EMO_MELTDOWN = [
    "WHY DOES EVERYTHING HURT",
    "I CAN’T KEEP DOING THIS",
    "THE VOID IS LOUD TONIGHT",
    "MY HEART IS A GLITCH",
    "EVERY WORD IS A WOUND"
]

ZERO_WIDTH_SPACE = "\u200B"
ZERO_WIDTH_JOINER = "\u200D"
ZERO_WIDTH_NONJOINER = "\u200C"
ZERO_WIDTH_NOBREAK = "\uFEFF"

INVISIBLE_SET = [
    ZERO_WIDTH_SPACE,
    ZERO_WIDTH_JOINER,
    ZERO_WIDTH_NONJOINER,
    ZERO_WIDTH_NOBREAK
]

LEET_CLASSIC = {
    "a": "4", "b": "8", "e": "3", "g": "6", "i": "1",
    "o": "0", "s": "5", "t": "7"
}

LEET_AGGRESSIVE = {
    "a": "/-\\", "b": "|3", "c": "(", "d": "|)", "e": "€",
    "f": "|=", "g": "9", "h": "|-|", "i": "!", "j": "_|",
    "k": "|<", "l": "1", "m": "/\\/\\", "n": "|\\|", "o": "◎",
    "p": "|*", "q": "0_", "r": "|2", "s": "$", "t": "7",
    "u": "|_|", "v": "\\/", "w": "\\/\\/", "x": "><",
    "y": "`/", "z": "2"
}

LEET_SYMBOLIC = {
    "a": "∆", "b": "ß", "c": "¢", "d": "ↁ", "e": "€",
    "f": "ƒ", "g": "₲", "h": "♄", "i": "!", "j": "¿",
    "k": "Ҡ", "l": "£", "m": "₥", "n": "₪", "o": "◎",
    "p": "þ", "q": "φ", "r": "®", "s": "§", "t": "†",
    "u": "µ", "v": "√", "w": "ω", "x": "✘", "y": "¥",
    "z": "ʐ"
}



class MutantSuite(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mutant‑Suite")
        self.setGeometry(200, 100, 1200, 700)
        self.setStyleSheet("background-color: #7b7b7b;")

        self.setWindowIcon(QIcon("mutantsuite_16.ico"))

        # Main layout
        main_layout = QHBoxLayout(self)

        # -----------------------------
        # LEFT PANEL: Mutation Buttons
        # -----------------------------
        left_container = QFrame()
        left_container.setStyleSheet("""
            QFrame {
                background-color: #1e1e1e;
                border-radius: 12px;
            }
        """)
        left_container.setFixedWidth(240)
        left_panel = QVBoxLayout(left_container)

        # Scroll area for mutation buttons
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setStyleSheet("QScrollArea { border: none; }")

        scroll_content = QWidget()
        scroll_content.setMinimumHeight(600)
        scroll_layout = QVBoxLayout(scroll_content)

        mutation_buttons = [
            "REVERSE MODE", "SPACE RANDOMIZER", "CODE INFUSER", "EMOJI INJECTOR",
            "CASE CHAOS", "GARBLER", "PUNC ROCK", "FANCIFIER",
            "BINARY", "LEETSPEEK", "EMO PHASE", "ZERO CHARACTER", "WORLDLY AESTHETICS",
        ]

        for name in mutation_buttons:
            btn = QPushButton(name)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #c83232;
                    color: white;
                    padding: 10px;
                    border-radius: 10px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #505050;
                }
            """)
            btn.clicked.connect(lambda _, n=name: self.load_tool_settings(n))
            scroll_layout.addWidget(btn)

        scroll_layout.addStretch()
        scroll_area.setWidget(scroll_content)

        left_panel.addWidget(scroll_area)
        main_layout.addWidget(left_container)

        # -----------------------------
        # CENTER PANEL: Tool Settings
        # -----------------------------
        self.settings_panel = QFrame()


        self.settings_panel.setFrameShape(QFrame.StyledPanel)
        self.settings_panel.setStyleSheet("""
            QFrame {
                background-color: #4b4b4b;
                border-radius: 12px;
            }
        """)


        settings_layout = QVBoxLayout(self.settings_panel)
        self.settings_panel.setLayout(settings_layout)

        self.settings_label = QLabel("Tool settings")
        self.settings_label.setFont(QFont("Arial", 14))
        self.settings_label.setStyleSheet("color: white;")
        main_layout.addWidget(self.settings_panel, 3)

        self.placeholder_label = QLabel("Select a mode to begin")
        self.placeholder_label.setStyleSheet("color: white; font-size: 16px; margin-top: 20px;")
        self.placeholder_label.setAlignment(Qt.AlignCenter)

        self.settings_panel.layout().addWidget(self.placeholder_label)

        # -----------------------------
        # RIGHT PANEL: Input/Output
        # -----------------------------
        self.right_panel = QVBoxLayout()

        # TOOL SETTINGS HEADER
        #tool_header = QLabel("Tool Settings")
        #tool_header.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        #self.right_panel.addWidget(tool_header)

        # SUBTLE DIVIDER LINE
        #divider = QFrame()
        #divider.setFrameShape(QFrame.HLine)
        #divider.setFrameShadow(QFrame.Sunken)
        #divider.setStyleSheet("color: #555; margin-bottom: 6px; margin-top: 2px;")
        #self.right_panel.addWidget(divider)

        # DYNAMIC MODULE UI CONTAINER
        #self.tool_settings_container = QWidget()
        #self.tool_settings_layout = QVBoxLayout(self.tool_settings_container)
        #self.right_panel.addWidget(self)

        # Container for dynamic module UI
        #self.tool_settings_container = QWidget()
        #self.tool_settings_layout = QVBoxLayout(self.tool_settings_container)
        #self.right_panel.addWidget(self.tool_settings_container)
        right_panel = QVBoxLayout()

        self.input_box = QTextEdit()
        self.output_box = QTextEdit()

        for box in (self.input_box, self.output_box):
            box.setStyleSheet("""
                QTextEdit {
                    background-color: #1e1e1e;
                    color: white;
                    border-radius: 10px;
                    padding: 10px;
                }
            """)

        right_panel.addWidget(QLabel("Input Text Box"))
        right_panel.addWidget(self.input_box)

        right_panel.addWidget(QLabel("Output Text Box"))
        right_panel.addWidget(self.output_box)

        # Generate button
        generate_btn = QPushButton("SAVE")
        generate_btn.clicked.connect(self.generate_output)
        generate_btn.setStyleSheet("""
            QPushButton {
                background-color: #c83232;
                color: white;
                padding: 12px;
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #7a00e6;
            }
        """)
        right_panel.addWidget(generate_btn)

        main_layout.addLayout(right_panel, 4)

    # -----------------------------
    # Safe layout clearing
    # -----------------------------
    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)

    # -----------------------------
    # Load settings for each module
    # -----------------------------
    def wrap_module_ui(self, parent_layout):
        container = QFrame()
        container.setStyleSheet("""
            QFrame {
                background-color: #333;
                border-radius: 10px;
                padding: 0px 12px 12px 12px;  /* remove top padding */
                margin-top: 10px;
            }
        """)

        inner = QVBoxLayout(container)
        parent_layout.addWidget(container)
        return inner

    def load_tool_settings(self, module_name):

        self.placeholder_label.hide()

        layout = self.settings_panel.layout()
        self.clear_layout(layout)

        layout.addWidget(self.settings_label)

        title = QLabel(f"{module_name}")
        title.setStyleSheet("color: white; font-size: 18px; font-weight: bold; margin-top: 6px;")
        layout.addWidget(title)

        inner = self.wrap_module_ui(layout)

        if module_name == "REVERSE MODE":
            desc = QLabel("Choose how to reverse the text:")
            desc.setStyleSheet("color: #cccccc;")
            inner.addWidget(desc)

            self.reverse_words_cb = QCheckBox("Reverse wording")
            self.reverse_words_cb.setStyleSheet("color: white;")
            inner.addWidget(self.reverse_words_cb)

            self.reverse_letters_cb = QCheckBox("Reverse letters")
            self.reverse_letters_cb.setStyleSheet("color: white;")
            inner.addWidget(self.reverse_letters_cb)

            apply_btn = QPushButton("Apply Reverse Mode")
            apply_btn.setStyleSheet("""
                QPushButton {
                    background-color: #444;
                    color: white;
                    padding: 8px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #666;
                }
            """)
            apply_btn.clicked.connect(self.apply_reverse_mode)
            inner.addWidget(apply_btn)


        if module_name == "SPACE RANDOMIZER":
            desc = QLabel("Choose a noise model for spacing:")
            desc.setStyleSheet("color: #cccccc;")
            inner.addWidget(desc)

            self.noise_radios = {}

            noise_types = [
                "Gaussian",
                "Uniform",
                "Poisson",
                "Exponential",
                "Bernoulli",
                "Gamma",
                "Beta"
            ]

            for nt in noise_types:
                rb = QRadioButton(nt)
                rb.setStyleSheet("color: white;")
                inner.addWidget(rb)
                self.noise_radios[nt] = rb

            self.noise_radios["Gaussian"].setChecked(True)

            apply_btn = QPushButton("Apply Noise")
            apply_btn.setStyleSheet("""
                QPushButton {
                    background-color: #444;
                    color: white;
                    padding: 8px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #666;
                }
            """)
            apply_btn.clicked.connect(self.apply_space_randomizer)
            inner.addWidget(apply_btn)

        if module_name == "CODE INFUSER":

            # Description
            desc = QLabel("Infuse text with code-like syntax:")
            desc.setStyleSheet("color: #cccccc;")
            inner.addWidget(desc)

            # Language label
            lang_label = QLabel("Select coding language:")
            lang_label.setStyleSheet("color: white;")
            inner.addWidget(lang_label)

            # --- SCROLLABLE LANGUAGE LIST ---
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

            # REMOVE the extra panel look
            scroll_area.setStyleSheet("""
                QScrollArea {
                    background: transparent;
                    border: none;
                }
                QScrollArea > QWidget {
                    background: transparent;
                }
                QScrollArea > QWidget > QWidget {
                    background: transparent;
                    margin: 0px;
                    padding: 0px;
                }
            """)

            inner.addWidget(scroll_area)

            scroll_content = QWidget()
            scroll_layout = QVBoxLayout(scroll_content)

            # Remove margins so the list starts flush at the top
            scroll_layout.setContentsMargins(0, 0, 0, 0)
            scroll_layout.setSpacing(4)

            scroll_area.setWidget(scroll_content)

            # Radio buttons stored here
            self.code_lang_radios = {}

            languages = [
                "Python", "JavaScript", "TypeScript", "C", "C++", "C#", "Java", "Kotlin",
                "Swift", "Go", "Rust", "Ruby", "PHP", "Perl", "Haskell", "Elixir",
                "Erlang", "Lisp", "Scheme", "R", "MATLAB", "HTML/XML", "CSS", "SQL",
                "Bash", "PowerShell"
            ]

            for lang in languages:
                rb = QRadioButton(lang)
                rb.setStyleSheet("color: white;")
                scroll_layout.addWidget(rb)
                self.code_lang_radios[lang] = rb

            # Default selection
            self.code_lang_radios["Python"].setChecked(True)

            # Frequency selector
            freq_label = QLabel("Infusion frequency (% of words):")
            freq_label.setStyleSheet("color: white;")
            inner.addWidget(freq_label)

            self.infuse_freq = QComboBox()
            self.infuse_freq.addItems(["10", "20", "30", "40", "50", "75", "100"])
            self.infuse_freq.setStyleSheet("color: white; background-color: #333;")
            inner.addWidget(self.infuse_freq)

            # Nesting toggle
            self.nesting_cb = QCheckBox("Allow nested containers")
            self.nesting_cb.setStyleSheet("color: white;")
            inner.addWidget(self.nesting_cb)

            # Apply button
            apply_btn = QPushButton("Apply Code Infuser")
            apply_btn.setStyleSheet("""
                QPushButton {
                    background-color: #444;
                    color: white;
                    padding: 8px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #666;
                }
            """)
            apply_btn.clicked.connect(self.apply_code_infuser)
            inner.addWidget(apply_btn)

        if module_name == "EMOJI INJECTOR":
            desc = QLabel("Build your emoji string (max 5 emojis):")
            desc.setStyleSheet("color: #cccccc;")
            inner.addWidget(desc)

            # --- SCROLLABLE EMOJI GRID ---
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            scroll_area.setStyleSheet("QScrollArea { border: none; }")
            inner.addWidget(scroll_area)

            scroll_content = QWidget()
            grid_layout = QGridLayout(scroll_content)
            scroll_area.setWidget(scroll_content)

            self.emoji_buttons = []
            row = 0
            col = 0

            for emoji in EMOJI_SET:
                btn = QPushButton(emoji)
                btn.setFixedSize(40, 40)
                btn.setStyleSheet("font-size: 20px;")
                btn.clicked.connect(lambda _, e=emoji: self.add_emoji_to_string(e))

                grid_layout.addWidget(btn, row, col)
                self.emoji_buttons.append(btn)

                col += 1
                if col >= 5:  # 5 emojis per row
                    col = 0
                    row += 1

            # Preview label
            self.emoji_preview = QLabel("Selected: ")
            self.emoji_preview.setStyleSheet("color: white; font-size: 18px;")
            inner.addWidget(self.emoji_preview)

            # Clear button
            clear_btn = QPushButton("Clear Emoji String")
            clear_btn.setStyleSheet("""
                QPushButton {
                    background-color: #444;
                    color: white;
                    padding: 6px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #666;
                }
            """)
            clear_btn.clicked.connect(self.clear_emoji_string)
            inner.addWidget(clear_btn)

            # Apply button
            apply_btn = QPushButton("Apply Emoji Injector")
            apply_btn.setStyleSheet("""
                QPushButton {
                    background-color: #444;
                    color: white;
                    padding: 8px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #666;
                }
            """)
            apply_btn.clicked.connect(self.apply_emoji_injector)
            inner.addWidget(apply_btn)

        if module_name == "CASE CHAOS":
            desc = QLabel("Choose a case mutation style:")
            desc.setStyleSheet("color: #cccccc;")
            inner.addWidget(desc)

            self.case_radios = {}

            case_modes = [
                "UPPERCASE",
                "lowercase",
                "Title Case",
                "sPoNgEbOb CaSe",
                "Random Chaos"
            ]

            for mode in case_modes:
                rb = QRadioButton(mode)
                rb.setStyleSheet("color: white;")
                inner.addWidget(rb)
                self.case_radios[mode] = rb

            # Default selection
            self.case_radios["Random Chaos"].setChecked(True)

            apply_btn = QPushButton("Apply Case Chaos")
            apply_btn.setStyleSheet("""
                QPushButton {
                    background-color: #444;
                    color: white;
                    padding: 8px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #666;
                }
            """)
            apply_btn.clicked.connect(self.apply_case_chaos)
            inner.addWidget(apply_btn)

        if module_name == "GARBLER":
            desc = QLabel("Choose your garbling style:")
            desc.setStyleSheet("color: #cccccc;")
            inner.addWidget(desc)

            self.garbler_radios = {}

            modes = [
                "Light Zalgo",
                "Medium Zalgo",
                "Heavy Zalgo",
                "Glitch Mode",
                "Digital Noise"
            ]

            for mode in modes:
                rb = QRadioButton(mode)
                rb.setStyleSheet("color: white;")
                inner.addWidget(rb)
                self.garbler_radios[mode] = rb

            self.garbler_radios["Medium Zalgo"].setChecked(True)

            apply_btn = QPushButton("Apply Garbler")
            apply_btn.setStyleSheet("""
                QPushButton {
                    background-color: #444;
                    color: white;
                    padding: 8px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #666;
                }
            """)
            apply_btn.clicked.connect(self.apply_garbler)
            inner.addWidget(apply_btn)

        if module_name == "PUNC ROCK":
            desc = QLabel("Choose your punctuation mayhem style:")
            desc.setStyleSheet("color: #cccccc;")
            inner.addWidget(desc)

            self.punc_radios = {}

            modes = [
                "Explosive",
                "Chaotic",
                "Overload",
                "ASCII Art",
                "Random Mix"
            ]

            for mode in modes:
                rb = QRadioButton(mode)
                rb.setStyleSheet("color: white;")
                inner.addWidget(rb)
                self.punc_radios[mode] = rb

            self.punc_radios["Random Mix"].setChecked(True)

            apply_btn = QPushButton("Apply Punc Rock")
            apply_btn.setStyleSheet("""
                QPushButton {
                    background-color: #444;
                    color: white;
                    padding: 8px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #666;
                }
            """)
            apply_btn.clicked.connect(self.apply_punc_rock)
            inner.addWidget(apply_btn)

        if module_name == "FANCIFIER":
            desc = QLabel("Choose a fancy Unicode font style:")
            desc.setStyleSheet("color: #cccccc;")
            inner.addWidget(desc)

            self.fancy_radios = {}

            styles = [
                "Cursive",
                "Bold Mono",
                "Fullwidth",
                "Script"
            ]

            for style in styles:
                rb = QRadioButton(style)
                rb.setStyleSheet("color: white;")
                inner.addWidget(rb)
                self.fancy_radios[style] = rb

            self.fancy_radios["Cursive"].setChecked(True)

            apply_btn = QPushButton("Apply Fancifier")
            apply_btn.setStyleSheet("""
                QPushButton {
                    background-color: #444;
                    color: white;
                    padding: 8px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #666;
                }
            """)
            apply_btn.clicked.connect(self.apply_fancifier)
            inner.addWidget(apply_btn)

        if module_name == "EMO PHASE":
            desc = QLabel("Choose your emo transformation style:")
            desc.setStyleSheet("color: #cccccc;")
            inner.addWidget(desc)

            self.emo_radios = {}

            modes = [
                "Blackletter",
                "Dramatic Tone",
                "Poetic Sadness",
                "Full Emo Meltdown"
            ]

            for mode in modes:
                rb = QRadioButton(mode)
                rb.setStyleSheet("color: white;")
                inner.addWidget(rb)
                self.emo_radios[mode] = rb

            # Default selection
            self.emo_radios["Blackletter"].setChecked(True)

            apply_btn = QPushButton("Apply Emo Phase")
            apply_btn.setStyleSheet("""
                QPushButton {
                    background-color: #444;
                    color: white;
                    padding: 8px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #666;
                }
            """)
            apply_btn.clicked.connect(self.apply_emo_phase)
            inner.addWidget(apply_btn)

        if module_name == "BINARY":
            desc = QLabel("Choose your binary encoding style:")
            desc.setStyleSheet("color: #cccccc;")
            inner.addWidget(desc)

            self.binary_radios = {}

            modes = [
                "ASCII Binary",
                "UTF-8 Binary",
                "Fake Hacker Mode"
            ]

            for mode in modes:
                rb = QRadioButton(mode)
                rb.setStyleSheet("color: white;")
                inner.addWidget(rb)
                self.binary_radios[mode] = rb

            self.binary_radios["ASCII Binary"].setChecked(True)

            apply_btn = QPushButton("Apply Binary Mode")
            apply_btn.setStyleSheet("""
                QPushButton {
                    background-color: #444;
                    color: white;
                    padding: 8px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #666;
                }
            """)
            apply_btn.clicked.connect(self.apply_binary_mode)
            inner.addWidget(apply_btn)

        if module_name == "ZERO CHARACTER":
            desc = QLabel("Choose your invisible character style:")
            desc.setStyleSheet("color: #cccccc;")
            inner.addWidget(desc)

            self.zero_radios = {}

            modes = [
                "Zero-Width Space",
                "Zero-Width Joiner",
                "Zero-Width Non-Joiner",
                "Invisible Mix",
                "Ghost Mode"
            ]

            for mode in modes:
                rb = QRadioButton(mode)
                rb.setStyleSheet("color: white;")
                inner.addWidget(rb)
                self.zero_radios[mode] = rb

            self.zero_radios["Invisible Mix"].setChecked(True)

            apply_btn = QPushButton("Apply Zero Character Mode")
            apply_btn.setStyleSheet("""
                QPushButton {
                    background-color: #444;
                    color: white;
                    padding: 8px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #666;
                }
            """)
            apply_btn.clicked.connect(self.apply_zero_character)
            inner.addWidget(apply_btn)

        if module_name == "LEETSPEEK":
            desc = QLabel("Choose your leetspeak style:")
            desc.setStyleSheet("color: #cccccc;")
            inner.addWidget(desc)

            self.leet_radios = {}

            modes = [
                "Classic 1337",
                "Aggressive Leet",
                "Symbolic Leet",
                "Random Mix"
            ]

            for mode in modes:
                rb = QRadioButton(mode)
                rb.setStyleSheet("color: white;")
                inner.addWidget(rb)
                self.leet_radios[mode] = rb

            # Default selection
            self.leet_radios["Classic 1337"].setChecked(True)

            apply_btn = QPushButton("Apply Leetspeak")
            apply_btn.setStyleSheet("""
                QPushButton {
                    background-color: #444;
                    color: white;
                    padding: 8px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #666;
                }
            """)
            apply_btn.clicked.connect(self.apply_leetspeak)
            inner.addWidget(apply_btn)

        if module_name == "WORLDLY AESTHETICS":
            desc = QLabel("Choose a world aesthetic to inject characters from:")
            desc.setStyleSheet("color: #cccccc;")
            inner.addWidget(desc)

            self.worldy_radios = {}

            aesthetics = [
                "Japanese",
                "Korean",
                "Chinese",
                "Russian",
                "Hindi",
                "Aramaic"
            ]

            for style in aesthetics:
                rb = QRadioButton(style)
                rb.setStyleSheet("color: white;")
                inner.addWidget(rb)
                self.worldy_radios[style] = rb

            # Default selection
            self.worldy_radios["Japanese"].setChecked(True)

            apply_btn = QPushButton("Apply Worldly Aesthetics")
            apply_btn.setStyleSheet("""
                QPushButton {
                    background-color: #444;
                    color: white;
                    padding: 8px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #666;
                }
            """)
            apply_btn.clicked.connect(self.apply_worldly_aesthetics)
            inner.addWidget(apply_btn)

        layout.addStretch()


    # -----------------------------
    # Space Randomizer logic (STACKING ENABLED)
    # -----------------------------
    def apply_space_randomizer(self):
        # Read from output first, fallback to input
        text = self.output_box.toPlainText() or self.input_box.toPlainText()
        output = ""

        # Determine selected noise type
        noise_type = None
        for nt, rb in self.noise_radios.items():
            if rb.isChecked():
                noise_type = nt
                break

        def get_spaces():
            if noise_type == "Gaussian":
                return max(0, int(random.gauss(1.5, 0.7)))
            elif noise_type == "Uniform":
                return random.randint(0, 4)
            elif noise_type == "Poisson":
                return np.random.poisson(1.2)
            elif noise_type == "Exponential":
                return int(np.random.exponential(1.0))
            elif noise_type == "Bernoulli":
                return 1 if random.random() < 0.3 else 0
            elif noise_type == "Gamma":
                return int(np.random.gamma(2.0, 0.8))
            elif noise_type == "Beta":
                return int(np.random.beta(2.0, 5.0) * 5)
            return 0

        for char in text:
            output += char + (" " * get_spaces())

        self.output_box.setPlainText(output)

    # -----------------------------
    # Code Infuser Logic (STACKING ENABLED)
    # -----------------------------
    def apply_code_infuser(self):
        text = self.input_box.toPlainText()
        if not text.strip():
            self.output_box.setPlainText("")
            return

        # Determine selected language
        selected_lang = None
        for lang, rb in self.code_lang_radios.items():
            if rb.isChecked():
                selected_lang = lang
                break

        words = text.split()

        # Formatting functions per language
        def python_format(w):
            return w.lower().replace(" ", "_")

        def javascript_format(w):
            parts = w.split()
            return parts[0].lower() + "".join(p.capitalize() for p in parts[1:])

        def typescript_format(w):
            return javascript_format(w) + ": any"

        def c_format(w):
            return f"{w};"

        def cpp_format(w):
            return f"std::{w};"

        def csharp_format(w):
            return f"{w} {{ get; set; }}"

        def java_format(w):
            return f"{w}();"

        def kotlin_format(w):
            return f"fun {w}()"

        def swift_format(w):
            return f"func {w}() {{}}"

        def go_format(w):
            return f"func {w}() {{}}"

        def rust_format(w):
            return f"let mut {w} = 0;"

        def ruby_format(w):
            return f"{w}\nend"

        def php_format(w):
            return f"${w} = null;"

        def perl_format(w):
            return f"my ${w};"

        def haskell_format(w):
            return f"{w} :: Int"

        def elixir_format(w):
            return f"def {w}(), do: :ok"

        def erlang_format(w):
            return f"{w}() -> ok."

        def lisp_format(w):
            return f"({w})"

        def scheme_format(w):
            return f"(define {w})"

        def r_format(w):
            return f"{w} <- NULL"

        def matlab_format(w):
            return f"{w} = 0;"

        def html_format(w):
            return f"<{w}>{w}</{w}>"

        def css_format(w):
            return f"{w}: value;"

        def sql_format(w):
            return w.upper()

        def bash_format(w):
            return f"${w}=$(echo value)"

        def powershell_format(w):
            return f"Set-{w} -Value 0"

        formatters = {
            "Python": python_format,
            "JavaScript": javascript_format,
            "TypeScript": typescript_format,
            "C": c_format,
            "C++": cpp_format,
            "C#": csharp_format,
            "Java": java_format,
            "Kotlin": kotlin_format,
            "Swift": swift_format,
            "Go": go_format,
            "Rust": rust_format,
            "Ruby": ruby_format,
            "PHP": php_format,
            "Perl": perl_format,
            "Haskell": haskell_format,
            "Elixir": elixir_format,
            "Erlang": erlang_format,
            "Lisp": lisp_format,
            "Scheme": scheme_format,
            "R": r_format,
            "MATLAB": matlab_format,
            "HTML/XML": html_format,
            "CSS": css_format,
            "SQL": sql_format,
            "Bash": bash_format,
            "PowerShell": powershell_format
        }

        formatter = formatters.get(selected_lang, lambda w: w)

        # Apply formatting
        transformed = [formatter(w) for w in words]

        self.output_box.setPlainText(" ".join(transformed))

    # -----------------------------
    # Apply Reverse Mode (STACKING ENABLED)
    # -----------------------------
    def apply_reverse_mode(self):
        # Read from output first, fallback to input
        text = self.output_box.toPlainText() or self.input_box.toPlainText()
        output = text

        if self.reverse_words_cb.isChecked():
            words = output.split()
            output = " ".join(reversed(words))

        if self.reverse_letters_cb.isChecked():
            output = " ".join(word[::-1] for word in output.split())

        self.output_box.setPlainText(output)

    # -----------------------------
    # Emoji Injector logic
    # -----------------------------

    def apply_emoji_injector(self):
        text = self.output_box.toPlainText() or self.input_box.toPlainText()

        if not hasattr(self, "emoji_string") or len(self.emoji_string) == 0:
            self.output_box.setPlainText(text)
            return

        words = text.split(" ")
        output_words = []

        for w in words:
            if random.random() < 0.25:
                output_words.append(self.emoji_string)
            output_words.append(w)

        self.output_box.setPlainText(" ".join(output_words))

    def add_emoji_to_string(self, emoji):
        if not hasattr(self, "emoji_string"):
            self.emoji_string = ""

        if len(self.emoji_string) < 5:
            self.emoji_string += emoji
            self.emoji_preview.setText(f"Selected: {self.emoji_string}")

    def clear_emoji_string(self):
        self.emoji_string = ""
        self.emoji_preview.setText("Selected: ")

    #
    # case chaos logic
    #

    def apply_case_chaos(self):
        text = self.output_box.toPlainText() or self.input_box.toPlainText()
        words = text.split()

        # Determine selected mode
        mode = None
        for name, rb in self.case_radios.items():
            if rb.isChecked():
                mode = name
                break

        def sponge_case(word):
            return "".join(
                c.upper() if random.random() < 0.5 else c.lower()
                for c in word
            )

        def random_chaos(word):
            styles = [
                str.upper,
                str.lower,
                str.title,
                lambda w: sponge_case(w)
            ]
            return random.choice(styles)(word)

        output_words = []

        for w in words:
            if mode == "UPPERCASE":
                output_words.append(w.upper())
            elif mode == "lowercase":
                output_words.append(w.lower())
            elif mode == "Title Case":
                output_words.append(w.title())
            elif mode == "sPoNgEbOb CaSe":
                output_words.append(sponge_case(w))
            elif mode == "Random Chaos":
                output_words.append(random_chaos(w))
            else:
                output_words.append(w)

        self.output_box.setPlainText(" ".join(output_words))

    def apply_garbler(self):
        text = self.output_box.toPlainText() or self.input_box.toPlainText()

        # Determine mode
        mode = None
        for name, rb in self.garbler_radios.items():
            if rb.isChecked():
                mode = name
                break

        # ZALGO INTENSITY
        if mode == "Light Zalgo":
            up_count = 1;
            mid_count = 1;
            down_count = 1
        elif mode == "Medium Zalgo":
            up_count = 3;
            mid_count = 2;
            down_count = 3
        elif mode == "Heavy Zalgo":
            up_count = 8;
            mid_count = 5;
            down_count = 8

        def zalgo_char(c):
            if c.strip() == "":
                return c
            up = "".join(random.choice(ZALGO_UP) for _ in range(up_count))
            mid = "".join(random.choice(ZALGO_MID) for _ in range(mid_count))
            down = "".join(random.choice(ZALGO_DOWN) for _ in range(down_count))
            return c + up + mid + down

        # GLITCH MODE
        def glitch_char(c):
            if c.strip() == "":
                return c
            noise = "".join(random.choice(GLITCH_CHARS) for _ in range(random.randint(1, 3)))
            return c + noise

        # DIGITAL NOISE MODE
        def digital_noise_char(c):
            if c.strip() == "":
                return c
            noise = "".join(random.choice(DIGITAL_NOISE) for _ in range(random.randint(1, 4)))
            return c + noise

        output = ""

        for c in text:
            if mode in ["Light Zalgo", "Medium Zalgo", "Heavy Zalgo"]:
                output += zalgo_char(c)
            elif mode == "Glitch Mode":
                output += glitch_char(c)
            elif mode == "Digital Noise":
                output += digital_noise_char(c)
            else:
                output += c

        self.output_box.setPlainText(output)

    # -----------------------------
    # Punc rock logic
    # -----------------------------

    def apply_punc_rock(self):
        text = self.output_box.toPlainText() or self.input_box.toPlainText()
        words = text.split()

        # Determine mode
        mode = None
        for name, rb in self.punc_radios.items():
            if rb.isChecked():
                mode = name
                break

        def pick_punc():
            if mode == "Explosive":
                return random.choice(PUNC_EXPLOSIVE)
            elif mode == "Chaotic":
                return random.choice(PUNC_CHAOTIC)
            elif mode == "Overload":
                return random.choice(PUNC_OVERLOAD)
            elif mode == "ASCII Art":
                return random.choice(PUNC_ASCII)
            elif mode == "Random Mix":
                all_punc = PUNC_EXPLOSIVE + PUNC_CHAOTIC + PUNC_OVERLOAD + PUNC_ASCII
                return random.choice(all_punc)
            return ""

        output_words = []

        for w in words:
            # 40% chance to add punctuation after each word
            if random.random() < 0.4:
                output_words.append(w + pick_punc())
            else:
                output_words.append(w)

        self.output_box.setPlainText(" ".join(output_words))

    def apply_fancifier(self):
        text = self.output_box.toPlainText() or self.input_box.toPlainText()

        # Determine selected style
        style = None
        for name, rb in self.fancy_radios.items():
            if rb.isChecked():
                style = name
                break

        fancy_map = FANCY_MAPS.get(style)
        if not fancy_map:
            self.output_box.setPlainText(text)
            return

        def fancy_char(c):
            if c.isalpha():
                idx = ord(c.lower()) - ord('a')
                if 0 <= idx < 26:
                    mapped = fancy_map[idx]
                    return mapped.upper() if c.isupper() else mapped
            return c

        output = "".join(fancy_char(c) for c in text)
        self.output_box.setPlainText(output)

    def apply_emo_phase(self):
        text = self.output_box.toPlainText() or self.input_box.toPlainText()
        words = text.split()

        # Determine mode
        mode = None
        for name, rb in self.emo_radios.items():
            if rb.isChecked():
                mode = name
                break

        # BLACKLETTER FONT
        def blackletter_char(c):
            if c.isalpha():
                idx = ord(c.lower()) - ord('a')
                if 0 <= idx < 26:
                    mapped = BLACKLETTER_MAP[idx]
                    return mapped.upper() if c.isupper() else mapped
            return c

        if mode == "Blackletter":
            output = "".join(blackletter_char(c) for c in text)
            self.output_box.setPlainText(output)
            return

        # DRAMATIC TONE
        if mode == "Dramatic Tone":
            output_words = []
            for w in words:
                if random.random() < 0.3:
                    w = w + " " + random.choice(DRAMATIC_PHRASES)
                output_words.append(w)
            self.output_box.setPlainText(" ".join(output_words))
            return

        # POETIC SADNESS
        if mode == "Poetic Sadness":
            output_words = []
            for w in words:
                if random.random() < 0.25:
                    output_words.append(random.choice(POETIC_SADNESS))
                output_words.append(w)
            self.output_box.setPlainText(" ".join(output_words))
            return

        # FULL EMO MELTDOWN
        if mode == "Full Emo Meltdown":
            output_words = []
            for w in words:
                if random.random() < 0.4:
                    output_words.append(random.choice(EMO_MELTDOWN))
                output_words.append(w.upper())
            self.output_box.setPlainText(" ".join(output_words))
            return

    def apply_binary_mode(self):
        text = self.output_box.toPlainText() or self.input_box.toPlainText()

        # Determine selected mode
        mode = None
        for name, rb in self.binary_radios.items():
            if rb.isChecked():
                mode = name
                break

        def ascii_binary(c):
            return format(ord(c), "08b")

        def utf8_binary(c):
            encoded = c.encode("utf-8")
            return " ".join(format(byte, "08b") for byte in encoded)

        def fake_hacker(c):
            b = format(ord(c), "08b")
            # Add glitchy spacing and grouping
            groups = [
                b[:4] + " " + b[4:],  # split in half
                b[0] + " " + b[1:4] + " " + b[4:],  # weird grouping
                " ".join(b),  # spaced bits
                b[::-1],  # reversed bits
            ]
            return random.choice(groups)

        output_bits = []

        for c in text:
            if mode == "ASCII Binary":
                output_bits.append(ascii_binary(c))
            elif mode == "UTF-8 Binary":
                output_bits.append(utf8_binary(c))
            elif mode == "Fake Hacker Mode":
                output_bits.append(fake_hacker(c))
            else:
                output_bits.append(c)

        self.output_box.setPlainText(" ".join(output_bits))

    def apply_zero_character(self):
        text = self.output_box.toPlainText() or self.input_box.toPlainText()

        # Determine selected mode
        mode = None
        for name, rb in self.zero_radios.items():
            if rb.isChecked():
                mode = name
                break

        def inject_zero(c, count=1):
            return c + "".join(random.choice(INVISIBLE_SET) for _ in range(count))

        output = ""

        for c in text:
            if mode == "Zero-Width Space":
                output += c + ZERO_WIDTH_SPACE

            elif mode == "Zero-Width Joiner":
                output += c + ZERO_WIDTH_JOINER

            elif mode == "Zero-Width Non-Joiner":
                output += c + ZERO_WIDTH_NONJOINER

            elif mode == "Invisible Mix":
                # 40% chance to inject a random invisible char
                if random.random() < 0.4:
                    output += inject_zero(c)
                else:
                    output += c

            elif mode == "Ghost Mode":
                # Heavy haunting: multiple invisible chars
                if random.random() < 0.7:
                    output += inject_zero(c, count=random.randint(2, 6))
                else:
                    output += c

            else:
                output += c

        self.output_box.setPlainText(output)

    def apply_leetspeak(self):
        text = self.output_box.toPlainText() or self.input_box.toPlainText()

        # Determine selected mode
        mode = None
        for name, rb in self.leet_radios.items():
            if rb.isChecked():
                mode = name
                break

        def convert_char(c, mapping):
            lower = c.lower()
            if lower in mapping:
                return mapping[lower]
            return c

        output = ""

        for c in text:
            if mode == "Classic 1337":
                output += convert_char(c, LEET_CLASSIC)

            elif mode == "Aggressive Leet":
                output += convert_char(c, LEET_AGGRESSIVE)

            elif mode == "Symbolic Leet":
                output += convert_char(c, LEET_SYMBOLIC)

            elif mode == "Random Mix":
                mapping = random.choice([LEET_CLASSIC, LEET_AGGRESSIVE, LEET_SYMBOLIC])
                output += convert_char(c, mapping)

            else:
                output += c

        self.output_box.setPlainText(output)

        #self.output_box.setPlainText(transformed)

    def apply_worldly_aesthetics(self):
        text = self.input_box.toPlainText()
        if not text.strip():
            self.output_box.setPlainText("")
            return

        # Determine selected aesthetic
        selected = None
        for style, rb in self.worldy_radios.items():
            if rb.isChecked():
                selected = style
                break

        charset = WORLDLY_SETS.get(selected, [])

        # Inject random characters
        transformed = ""
        for ch in text:
            if ch.isalpha() and random.random() < 0.3:  # 30% chance to mutate
                transformed += random.choice(charset)
            else:
                transformed += ch

        self.output_box.setPlainText(transformed)

    # -----------------------------
    # Generate output (basic version)
    # -----------------------------
    def generate_output(self):
        text = self.output_box.toPlainText()

        if not text.strip():
            return  # nothing to save

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Output Text",
            "",
            "Text Files (*.txt);;All Files (*)"
        )

        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(text)
            except Exception as e:
                print("Error saving file:", e)

    # -----------------------------
    # Apply Reverse Mode
    # -----------------------------
    def apply_reverse_mode(self):
        text = self.input_box.toPlainText()
        output = text

        if self.reverse_words_cb.isChecked():
            words = output.split()
            output = " ".join(reversed(words))

        if self.reverse_letters_cb.isChecked():
            output = " ".join(word[::-1] for word in output.split())

        self.output_box.setPlainText(output)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MutantSuite()
    window.show()
    sys.exit(app.exec_())
