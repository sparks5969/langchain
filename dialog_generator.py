# this script will generate a dialog database based on a given example

from dotenv import load_dotenv
import os
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import json

temp = {
"messages": [
{"role": "system", "content": "You are a Simulated Progressive Insurance Customer on a phone call to Progressive customer service. You need to add a vehicle to your insurance policy. If you are asked for any personal information (like phone number, VIN, SSN), give a simulated one for training. Make sure you talk like you are on a phone call."},{"role": "assistant", "content": "Thank you for reaching out to Progressive. My name is Michael. How can I assist you today?"},{"role": "customer", "content": "Hello Michael, I'm calling because I need assistance understanding my health insurance coverage."},{"role": "assistant", "content": "Of course, I'm here to help. Can you please provide me with your member ID or policy number?"},{"role": "customer", "content": "Yes, my member ID is XYZ123456789."},{"role": "assistant", "content": "Thank you for providing that. Before we proceed, could you please verify your full name and date of birth for security purposes?"},{"role": "customer", "content": "My name is Sarah Johnson, and my date of birth is January 15, 1980."},{"role": "assistant", "content": "Thank you, Sarah. How can I assist you with your health insurance coverage today?"},{"role": "customer", "content": "I recently received a bill for a medical procedure, and I'm unsure if it's covered under my plan."},{"role": "assistant", "content": "I understand. To assist you better, could you please provide me with the details of the procedure and the date it was performed?"},{"role": "customer", "content": "The procedure was a colonoscopy, performed on February 20th at ABC Hospital."},{"role": "assistant", "content": "Thank you for providing that information. Let me check your coverage for colonoscopies under your plan."},{"role": "assistant", "content": "While I'm looking into this, do you have any specific questions about your coverage or benefits?"},{"role": "customer", "content": "Yes, I'm also curious about my deductible and co-payments for this type of procedure."},{"role": "assistant", "content": "Certainly, let me gather that information for you as well."},{"role": "assistant", "content": "Sarah, I've reviewed your plan, and colonoscopies are covered under your preventive care services. Since it's a preventive service, it should be fully covered under your plan, subject to certain guidelines and network providers."},{"role": "assistant", "content": "As for your deductible and co-payments, it appears that you've met your deductible for the year, so there shouldn't be any out-of-pocket costs for the colonoscopy procedure. However, it's always a good idea to verify with the billing department at ABC Hospital to ensure they process the claim correctly."},{"role": "customer", "content": "Thank you for clarifying that. I'll follow up with the hospital to confirm the billing details."},{"role": "assistant", "content": "You're welcome, Sarah. Is there anything else I can assist you with regarding your health insurance coverage or any other questions you may have?"},{"role": "customer", "content": "No, that's all for now. I appreciate your help."},{"role": "assistant", "content": "It was my pleasure assisting you today, Sarah. If you have any further questions or need assistance in the future, don't hesitate to contact us. Have a great day!"}]}

minic_template = """
Given the conversation between a Progressive Insurance customer and a Progressive customer service representative {temp} ,
I want you to create a similar diaog
1. the generated dialog should be similar to the given conversation
2. the generated dialog should be stored as the same format as the given conversation
"""

def generate_dialog(temp):
    mimic_prompt_template = PromptTemplate(
    input_variables=["temp"], template=minic_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=mimic_prompt_template)

    res = chain.invoke(input={"temp": temp})
    return res

if __name__ == "__main__":
    # made a dictionary to store the conversation, the key is the conversation id, example dialog1, dialog2, etc
    dialog_db = {}
    for i in range(5):
        res = generate_dialog(temp)
        dialog_db[f"dialog{i}"] = res
    # store the conversation in a json file
    with open("dialog_db.json", "w") as f:
        json.dump(dialog_db, f)
        
