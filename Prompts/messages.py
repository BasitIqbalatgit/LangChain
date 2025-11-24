# Messages:
# There are 3 main type of messages :
# 1. SystemMessage: the message that is passed to the Model as an instruction (i.e you are a Best Ai engineer ... )
# 2. HummanMessage: the message that is a human prompt passed to the model (i.e what is the capital of pakistan)
# 3. AIMessage: the message that is a response from the model (i.e capital of pakistan is islamabad)

# Why use Messages : Becz the chat_history becomes large and we can not identify which message is human prompt which is ai response
# e.g ['hi', 'hello i am agent', ' what is the biggest number 2 or 0', '2 is the largest number'] 
# can not identify which is human message and which is the response from the ai
# so we use Messages to identify them 