from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate , HumanMessagePromptTemplate , SystemMessagePromptTemplate

model=ChatOllama(model='llama3.2:latest',
                 top_k=20,
                 temperature=0.7,
                 top_p=0.5)

def run_prompt(person):
    system=SystemMessagePromptTemplate.from_template('You are my {person} good at {subject}')
    human=HumanMessagePromptTemplate.from_template('{doubt}')
    prompt=ChatPromptTemplate.from_messages([system,human])

    chain=prompt | model
    result=chain.invoke({"person":person,"subject":"machine learning","doubt":"What is machine learning"})
    name=person+".txt"
    file=open(name,'w')
    file.write(result.content)
    print("Wrote to file",name)

run_prompt('teacher')
run_prompt('friend')