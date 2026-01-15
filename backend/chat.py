from langchain_core.prompts import ChatPromptTemplate , HumanMessagePromptTemplate , SystemMessagePromptTemplate
from models import chatModel

def run_prompt(person):
    system=SystemMessagePromptTemplate.from_template('You are my {person} good at {subject}')
    human=HumanMessagePromptTemplate.from_template('{doubt}')
    prompt=ChatPromptTemplate.from_messages([system,human])

    chain=prompt | chatModel
    result=chain.invoke({"person":person,"subject":"machine learning","doubt":"What is machine learning"})
    name=person+".txt"
    file=open(name,'w')
    file.write(result.content)
    print("Wrote to file",name)

