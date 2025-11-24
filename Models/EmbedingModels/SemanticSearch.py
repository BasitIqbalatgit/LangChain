from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

cricketers = [
    "Babar Azam:\n- Elegant right-handed batter\n- Master of cover drives\n- Former all-formats captain\n- ODI run machine\n- One of the most consistent players in the world",

    "Shaheen Shah Afridi:\n- Left-arm fast bowler\n- Deadly with the new ball\n- Known for dramatic early breakthroughs\n- T20 specialist in powerplay overs\n- Pakistan’s frontline strike bowler",

    "Mohammad Rizwan:\n- Wicketkeeper-batter\n- High-intensity innings builder\n- Outstanding in chases\n- Consistent T20 performer\n- Known for fitness and work ethic",

    "Shadab Khan:\n- Leg-spinning all-rounder\n- Dynamic fielder\n- Reliable lower-order hitter\n- Key middle-overs controller\n- Vice-captaincy experience",

    "Fakhar Zaman:\n- Aggressive left-handed opener\n- Known for fearless stroke play\n- Match-winner in ICC events\n- ODI double-centurion\n- Dangerous against pace"
]


embeddings = HuggingFaceEndpointEmbeddings(
    repo_id= "sentence-transformers/all-MiniLM-L6-v2",
    task="feature-extraction",
)

cricketers_embeddings = embeddings.embed_documents(cricketers)

query = "Who is the left-arm fast bowler in the world?"
query_embedding = embeddings.embed_query(query)

cosine_similarity_index= cosine_similarity([query_embedding], cricketers_embeddings)

answer_index = sorted(list(enumerate(cosine_similarity_index[0])), key=lambda x: x[1], reverse=True)[0][0]
answer= cricketers[answer_index]
print("Question: ", query)
print("Answer: ", answer)
print("Similarity Score: ", cosine_similarity_index[0][answer_index])