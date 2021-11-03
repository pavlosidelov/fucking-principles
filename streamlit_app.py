import random as rnd
#import icecream as ic
#import pickledb
import streamlit as st
#import db_ops


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

fp_base = ['When in doubt fucking Red Team it.',
'Be fucking bold.',
'There is no fucking box.',
'Always fucking deliver.',
'Learn from your fucking mistakes.',
'Build fucking credibility.',
'Be more fucking efficient.',
'Carve your own fucking path.',
'Make it fucking asymmetrical.',
'Learn to fucking say no.',
'Don’t plan or design in a fucking vacuum.',
'Ask good fucking questions.',
'Show some fucking passion.',
'Fucking systems and networks.',
'Be fucking observant.',
'Act, don’t fucking react.',
'Set some fucking goals.',
'Pay attention to fucking details.',
'It’s not what you say, it’s how you fucking say it.',
'Drink more fucking coffee.',
'Work outside your fucking comfort zone.',
'Fucking motivate your team and others.',
'Defy fucking convention.',
'Proof your fucking copy.',
'Be fucking accountable.',
'Never take no for a fucking answer.',
'Learn to fucking take advice.',
'Start a fucking side project.',
'Keep fucking learning.',
'Learn to fucking improvise.',
'Master your fucking craft.',
'Fucking fuck buzzwords.',
'Sanitize your fucking input.',
'Work with reliable fucking people.',
'Backup your fucking data.',
'Always be fucking ready.',
'Assumption is the mother of all fucking fuckups.',
'The solution is in the fucking problem.',
'Always have a fucking escape plan.',
'Never fucking get caught.']

rule_base = [
    'Rule 0: Always double-tap',
    'Rule 1: Always have an escape plan. \n The 3 Plans - Rule 1 extension \n 1. Always have a plan. \n 2. Always have a back-up plan, because the first one probably won’t work. \n 3. Always have an escape plan because all the rest of the plans will fail. \n Remember PACE: Primary, Alternate, Contingency and Emergency.',
    'Rule 2: Be aware of your surroundings.',
    'Rule 3: Assumption is the mother of all fuckups.',
    'Rule 4: Always have a backup plan.',
    'Rule 5: Never get caught.',
    'Rule 6: Keep your mouth shut.',
    'Rule 7: KISS: Keep it simple, stupid.',
    'Rule 8: 7 Ps: Proper Planning and Preparation Prevents \n Piss Poor Performance',
    'Rule 9: Plan, execute and vanish.',
    'Rule 10: Always invest in good quality.',
    'Rule 11: Trust your gut.',
    'Rule 12: Always carry a knife.',
    'Rule 13: Do one thing at a time.',
    'Rule 14: Pick your battles…',
    'Rule 15: Simple and light equals freedom, agility and mobility.',
    'Rule 16: Target dictates the weapon \n and the weapon dictates the movement. \n ("Mack" Machowicz)',
    'Rule 17: Use ACTE: assess the situation; \n create a simple plan; \n take action and evaluate your progress. \n ("Mack" Machowicz)',
    'Rule 18: Don’t believe what you’re told. Double check.',
    'Rule 19: Hide in plain sight. Blend in.',
    'Rule 20: Think like a man of action, act like a man of thought.',
    'Rule 21: The more sophisticated the technology \n the more vulnerable it is to primitive attacks. \n People often overlook the obvious.',
    'Rule 22: If you’re happy with your security, so are the bad guys.',
    'Rule 23: “Bad guys attack, and good guys react” \n is not a viable security strategy.',
    'Rule 24: An adversary is most vulnerable to detection \n and disruption just prior to an attack.',
    'Rule 25: Low-tech attacks work (even against high-tech devices and systems).',
    'Rule 26: Never mess with a man’s coffee.',
    'Rule 27: Don’t spend time trying to move your opponent, just move yourself.',
    'Rule 28: The quality of your friends always matters more than the quantity.',
    'Rule 29: Always provide correction in private and praise in public.',
    'Rule 30: Opening the door for a lady is not optional.',
    'Rule 31: You can do big things with a small team.',
    'Rule 32: Don’t go into debt.',
    'Rule 33: Do not publish your life online, \n keep your life private.',
    'Rule 34: The GORUCK Rule - Under promise and over deliver.',
    'Rule 35: Progress comes to those who train and train; \n reliance on secret techniques will get you nowhere. \n (Morihei Ueshiba)',
    'Rule 36: You must understand that there is more than one path to the top of the mountain. \n (Miyamoto Musashi)',
    'Rule 37: To know ten thousand things, know one well. \n (Musashi)',
    'Rule 38: You are what you do when it counts.',
    'Rule 39: If you think it was too easy, it was a trap. \n Look for jumping guards coming from the sides.',
    'Rule 40: The bad guys don’t obey our security policies.',
    'Rule 41: If there’s a question about if it’s necessary, remove it. \n Less is more and more is lazy. \n (Jason McCarthy, GORUCK founder)',
    'Rule 42: Once is an accident. Twice is coincidence. Three times is an enemy action.',
    'Rule 43: Never do the same thing twice.',
    'Rule 44: Always take care of your team first, then your gear and finally yourself.',
    'Rule 45: Check the crowd: \n who is staring at you, who is all the sudden silent when you enter.',
    'Rule 46: Always sit with your back to the wall, \n even when there are mirrors you can use.',
    'Rule 47: Never take the elevator.',
    'Rule 48: The solution is in the problem.',
    "Rule 49: Fail to Red Team and everything will go according to plan—right up \n to the point it doesn't. \n (Red Team Journal)",
    "Rule 50: If it's stupid but works, it isn't stupid.",
    'Rule 51: Don’t play by the rules.',
    'Rule 52: Don’t become predictable.',
    'Rule 53: Our fucks are our fucks alone to give. \n (Patrick Rhone)',
    'Rule 54: Plans are useless, but planning is indispensable. \n (Dwight D. Eisenhower)',
    'Rule 55: Act, don’t react.',
    'Rule 56: Shitty situations inspire brilliant solutions.',
    'Rule 57: Establish baselines. \n Look for anomalies. \n Have a plan.',
    'Rule 58: If you want truly to understand something, try to change it.',
    "Rule 59: Expectations = Disappointment. \n Don't expect anything.",
    'Rule 60: You don’t have to like it, you just have to do it.',
    'Rule 61: Understand. Anticipate. Adapt. \n (Red Team Journal)',
    'Rule 62: Real attackers will make you patch your people.',
    'Rule 63: First you check, then you double-check. Finally you commit.',
    'Rule 64: He who angers you conquers you.',
    'Rule 65: Find a way to succeed.',
    'Rule 66: Clap only when you are impressed.',
    "Rule 67: Once is an accident, twice is... \n Huh… No, I don't believe in coincidences. \n Twice is enemy action. \n (overwrites Rule 42).",
    'Rule 68: Add things until it starts sucking, \n take things away until it stops getting better. \n(Frank Chimero)',
    'Rule 69: GLBYS: Gary, look before you sit.',
    "Rule 70: If you can't be smart, you better be strong.",
    'Rule 71: Be hard to break.',
    'Rule 72: Every time you train, \n train with the motivation and purpose \n hat you will be the hardest person someone ever tries to kill. \n (Tim Kennedy)',
    'Rule 73: Tremendous detailed planning, violent execution.',
    ""
]

total_fp_base = len(fp_base)
total_rule_base = len(rule_base)
print("Total FB : ", total_fp_base)

#Get Fucking Principle
def get_fp():
    fp_num = rnd.randrange(0, total_fp_base-1, 1)
    print("FP NUM : ", fp_num)
    fp_quote = fp_base.pop(fp_num)
    print("Quote : ", fp_quote)
    return fp_quote

#Get Fucking Principle
def get_rule():
    rule_num = rnd.randrange(0, total_rule_base-1, 1)
    print("Rule NUM : ", rule_num)
    rule_quote = rule_base.pop(rule_num)
    print("Quote : ", rule_quote)
    return rule_quote

st.image("fucking_logo.png")
fucking_quote = get_fp()
rule_quote = get_rule()
print("Main fucking quote - ", fucking_quote)
fq = st.title(fucking_quote)
rq = st.text(rule_quote)
get_fucking_button = st.button('Get Fucking Principle')
with fq:
    fq = get_fp()
    rq = get_rule()

#-------------- FOOTER ---------------
from htbuilder import * #HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))

def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)

def layout(*args):
    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """
    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)
        elif isinstance(arg, HtmlElement):
            body(arg)
    st.markdown(str(foot), unsafe_allow_html=True)

def footer():
    myargs = [
        "Inspired by ",
        image('https://static1.squarespace.com/static/511d8f3ae4b02acb17b5ced9/t/574ad664b6aa60d8439ffea1/1608546984814/?format=1500w',
              width=px(60), height=px(25)),
        link("https://redteams.net/rules", "REDTEAMS.NET"),
        br(),
        link("mailto:info@fuckingprinciples.xyz", "Send Us Fucking Mail"),
    ]
    layout(*myargs)

footer()
#-------------- FOOTER ---------------
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
