import streamlit as st

#Let x be the measure of the contentedness of a human's existence.
st.sidebar.write("The following is a python program that calculates a person’s contentedness based on their responses to the inventory below. The measured emotions are from Paul Ekman’s research on the fundamental emotions – in essence the primary colors of our feelings.")
st.sidebar.write("Let x be the measure of the contentedness of a human's existence.")
st.sidebar.write("The following values are completely based on personal subjective experience, and the questions are specific to my life (for now)")
st.sidebar.write("The emotions are on a scale of 100.")
st.sidebar.write("Enter your own values for your current experience of each emotion. Think of a number that you feel is a rolling average of your last week.")
st.sidebar.write("At the end, you will be asked what aspect of your life is most important to you. For now, answer the following questions.")







#Psychologist Paul Ekman defined 6 emotions that are universally experienced in all cultures: happiness, fear, anger, sadness, disgust, and surprise.
#Let's assume every person starts out with a balance of each core emotion.
#Some emotions are combinations of the core emotions and will be expressed accordingly.
#In this program, the emotions have a minimum value of 0 and maximum value of 100


st.sidebar.title("Contentedness Level Calculator")


happiness = st.sidebar.number_input("Enter your happiness on a scale of 1- 100", min_value=1, max_value=100, step=1)
fear = st.sidebar.number_input("Enter your fear on a scale of 1- 100", min_value=1, max_value=100, step=1)
anger = st.sidebar.number_input("Enter your anger on a scale of 1- 100", min_value=1, max_value=100, step=1)
sadness = st.sidebar.number_input("Enter your sadness on a scale of 1- 100", min_value=1, max_value=100, step=1)
disgust = st.sidebar.number_input("Enter your disgust on a scale of 1- 100", min_value=1, max_value=100, step=1)
surprise = st.sidebar.number_input("Enter your surprise on a scale of 1-100", min_value=1, max_value=100, step=1)
if surprise:
    st.sidebar.write("Psychologist Paul Ekman defined 6 emotions that are universally experienced in all cultures: happiness, fear, anger, sadness, disgust, and surprise.")
    st.sidebar.write("Some emotions (cockiness, curiosity, regret, impatience, loneliness, envy) are combinations of the core emotions and will be expressed accordingly.")
    st.sidebar.write("In this program, the emotions have a minimum value of 0 and maximum value of 100")

soccer_team_won = st.sidebar.radio("Have you had a significant accomplishment in the past 3 months?", ('Yes, I have succeeded at a hobby, sport, or pursuit that is personally meaningful', 'Yes, I have had significant professional or academic success', 'No'))
if soccer_team_won == "Yes, I have succeeded at a hobby, sport, or pursuit that is personally meaningful":
    st.sidebar.write("I scored a goal in my playoff match for Lakeview Men’s Soccer. My best friends are on the soccer team- I'm always happy playing with them.")
if soccer_team_won == "Yes, I have had significant professional or academic success":
    st.sidebar.write("I got an A on my Physics midterm. Physics is a hard class, and it's nice when I get an A.")

number_of_olives_consumed = st.sidebar.number_input("Have you endured a very distasteful event in the last three months?", min_value=0, max_value=100, step=1)
if number_of_olives_consumed >= 1:
    st.sidebar.write("For me, it’s eating olives. Olives taste like rubber. Seeing them every day at my pizza job adds to my resentment.")

had_physics_class = st.sidebar.radio("Did you learn something meaningful today?", ('Yes', 'No'))
if had_physics_class == "Yes":
    st.sidebar.write("Starting a new unit in physics is thrilling.")
    st.sidebar.write("There is so much I still have to learn about physics – every day is filled with curiosity of the unknown.")
if had_physics_class == "No":
    st.sidebar.write("Damn, the clutter and clunk of life can get in the way.")

number_of_pets = st.sidebar.number_input("How many pets do you have", min_value=0, max_value=100, step=1)
st.sidebar.write("Note: Any number of fish is still equal to 1 pet")
st.sidebar.write("I love my dogs.")
st.sidebar.write("But I still have to clean up their puke or wash them in the shower because they rolled in a deer carcass.")

visited_grandparents = st.sidebar.radio("Have you spent time with your extended family members recently?", ('Yes', 'No'))
if visited_grandparents == "Yes":
    st.sidebar.write("The trip to my grandparent’s house in Chicago for Thanksgiving and Christmas always makes me happy.")

relationship_ended = st.sidebar.radio("Did you have a important relationship which ended in the last 8 weeks?", ('Yes', 'No'))

bournemouth_won = st.sidebar.radio("Did your favorite sports team win this week's matchup?", ('Yes', 'No'))
if bournemouth_won == "Yes":
    st.sidebar.write("My favorite sports team is A.F.C. Bournemouth, which is a small soccer team on the South Coast of England.")

chicagobears_won = st.sidebar.radio("Did the Chicago Bears win their matchup today?", ('Yes', 'No'))
if chicagobears_won == "Yes":
    st.sidebar.write("My favorite American sports team. Winning is unlikely.")
if chicagobears_won == "No":
    st.sidebar.write("I got used to them losing so much that I don't get sad anymore. I just get less happy.")
the_big_question = st.sidebar.selectbox("What part of your life is most important to you?", ('Work', 'Family', 'Leisure'))
if the_big_question:
    st.sidebar.write("True contentedness is a careful balance of each core emotion. However, the distribution of these emotions is different depending on what you value.")


if number_of_pets >= 2:
    happiness += 8 * number_of_pets
    disgust += 2 * number_of_pets

loneliness = (.5 * sadness) + (.5 * fear)
if relationship_ended == 'Y':
    anger += 20
    fear += 15
    sadness += 5
    loneliness *= 40

if relationship_ended == 'N':
    surprise += 10

if soccer_team_won == "Yes, I have succeeded at a hobby, sport, or pursuit that is personally meaningful":
    happiness *= 1.25
    fear -= 5
    sadness //= 1.25

if soccer_team_won == "Yes, I have had significant professional or academic success":
    happiness *= 1.05
    fear -= 10
    sadness //= 1.25


if soccer_team_won == "No":
    happiness *= .75

if number_of_olives_consumed >= 1:
    disgust += 10

cockiness = (.33 * disgust) + (.33 * happiness) + (.33 * fear)
envy = (.50 * sadness) + (.50 * fear)
if bournemouth_won == 'Y':
    happiness += 5
    cockiness += 10

if bournemouth_won == 'N':
    envy += 10

curiosity = (.50 * happiness) + (.30 * fear) + (.20 * cockiness)
impatience = (.75 * anger) + (.25 * fear)
if had_physics_class == 'Y':
    happiness *= 2
    curiosity *= 2

if had_physics_class == 'N':
    impatience += 10
    happiness -= 2

if chicagobears_won == 'Y':
    happiness += 5

if chicagobears_won == 'N':
    disgust += 5
    happiness -= 5

regret = (.30 * sadness) + (.70 * fear)
if visited_grandparents == 'Y':
    happiness += 15
    sadness += 10
    regret *= 1.5
    anger -= 10

if visited_grandparents == 'N':
    regret *= 3
    anger += 10


happiness = max(min(happiness, 100), 1)
fear = max(min(fear, 100), 1)
anger = max(min(anger, 100), 1)
sadness = max(min(sadness, 100), 1)
disgust = max(min(disgust, 100), 1)
surprise = max(min(surprise, 100), 1)

button = st.button("When you have answered every question, press this button to get your contentedness level")
if button:
    if the_big_question == 'Work':
        contentedness_work = (.20 * fear) + (.40 * anger) + (.40 * disgust)
        st.write("Your contentedness level is: ", contentedness_work)
        if contentedness_work >= 0 and contentedness_work <= 50:
            st.write("You don’t seem very content. I used to measure my performance, progress, and satisfaction daily. But, I can be hard on myself, and my brain is geared toward optimization. So, the obsessive measurement actually reduced how good I felt.")
            st.write("Progress is a trend line with an r value <1. You’re going to have good and bad days on the climb.")
        elif contentedness_work > 51:
            st.write("You seem to be very content.")

    elif the_big_question == 'Family':
        contentedness_fam = (.50 * happiness) + (.10 * fear) + (.30 * sadness) + (.10 * disgust)
        st.write("Your contentedness level is: ", contentedness_fam)
        if contentedness_fam >= 0 and contentedness_fam <= 50:
            st.write("Your contentedness is low. I’ve learned that sometimes contentedness is accepting that love is a challenge.")
        elif contentedness_fam > 51:
            st.write("You are balanced and content. Say hi to your people for me.")

    elif the_big_question == 'Leisure':
        contentedness_leisure = (.20 * happiness) + (.20 * fear) + (.20 * anger) + (.20 * sadness) + (.20 * disgust)
        st.write("Your contentedness level is: ", contentedness_leisure)
        if contentedness_leisure >= 0 and contentedness_leisure <= 50:
            st.write("You seem to not be very content. I suggest caring for another pet or taking on something new. Burning through a season on Netflix is great, but I think meaningful leisure is assuming a challenge or responsibility that doesn’t make money or lines on a resume.")
        elif contentedness_leisure > 51:
            st.write("You are balanced and content. You should buy bag of chips to go along with your TV watching.")

    st.write("As for myself, my calculated contentedness level is 61.5. That’s my x. A single value which represents me, right now, at this very moment in time. The beauty of life is that it's constantly changing. If you were content all the time, there would be no reason to try new things, meet new people, or invent something revolutionary. Contentedness represents the changing nature of life. So does x.")
