from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, RadioField, SubmitField
from wtforms.validators import Length, InputRequired, ValidationError, NumberRange
class PredictionForm(FlaskForm):
    Qn1 = RadioField("What is your noise level at a meeting with friends?", choices=[(0, 'Mostly High'), (1, 'Mostly Low')], validators=[InputRequired()])
    Qn2 = RadioField("What do you usually do when attending a new meeting?", choices=[(0, 'I tend to only answer incoming questions'), (1, 'I tend to get involved in the overall conversation')], validators=[InputRequired()])
    Qn3 = RadioField("What is your reaction when a talkative person talks to you at a gathering?", choices=[(0, 'I respond well naturally, and continue the conversation'), (1, 'I dont know what to say and its burdensome')], validators=[InputRequired()])
    Qn4 = RadioField("What is your reaction when your ideal type says you are attractive?", choices=[(0, 'I wonder where that person is attracted to'), (1, 'I already fantasized about dating this person')], validators=[InputRequired()])
    Qn5 = RadioField("What is your reaction when a friend suddenly asked you what you would be doing in 10 years?", choices=[(0, 'I dont know? I have no idea'), (1, 'Will I ever be a successful person?')], validators=[InputRequired()])
    Qn6 = RadioField("If you were given a new job, what would you choose?", choices=[(0, 'Tasks with clear guidelines'), (1, 'Tasks that I can freely apply my thoughts')], validators=[InputRequired()])
    Qn7 = RadioField("What do you care more about when talking to someone?", choices=[(0, 'Conversation topic and flow'), (1, 'Speech and expression')], validators=[InputRequired()])
    Qn8 = RadioField("You see your friend do something wrong, what do you do?", choices=[(0, 'I honestly talk to my friend about it'), (1, 'I make my friend aware of their faults indirectly')], validators=[InputRequired()])
    Qn9 = RadioField("What do you do when a new cafe opens near your home?", choices=[(0, 'Oh, a brand new cafe, Ill have to try it soon'), (1, 'Its closer than the cafe i used to go to. I may go there tomorrow after work to try')], validators=[InputRequired()])
    Qn10 = RadioField("When you invite your friends to your house, what do you do?", choices=[(0, 'I set the menu for number of attendees, and if food is insufficient I order more'), (1, 'I clearly prepare the menu for the right quantity in adavance')], validators=[InputRequired()])
    submit = SubmitField("Predict")