from dotenv import load_dotenv
import os
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from third_parties.linkedin import scrape_linkedin_profile
import json



if __name__ == "__main__":
    print("This is a langchain program")


    summary_template = """
    given the Linkedin information {information} about a person I want to you to create
    1. a short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url='https://www.linkedin.com/in/sining-wang-7267aa7a/')
    
    res = chain.run(information=linkedin_data)
    print(res)