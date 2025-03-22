from generate import generate_response

#this will create the seo blog outline for the topic 
def create_outline(topic):
    print("📝 Creating blog outline...")
    prompt = f"Create an SEO-friendly blog outline on {topic}."
    return generate_response(prompt)

# this will generate the blog based on the  outline from the create_outline() method
def generate_blog(topic, outline):
    print("✍️ Generating blog content...")
    prompt = f"Write a well-structured SEO-optimized blog (at least 2000 words) on {topic} using this outline:\n{outline}"
    return generate_response(prompt)

# this will optimize the generated blog into seo  and add  keywords
def optimize_seo(content):
    print("📈 Optimizing for SEO...")
    prompt = f"Optimize the following blog for SEO. Add relevant keywords, meta descriptions, and improve readability:\n{content}"
    return generate_response(prompt)

# this will check for spelling mistake, grammer in the generated blog 
def review_content(content):
    print("🔍 Reviewing and finalizing the blog...")
    prompt = f"Proofread the following blog for grammar, clarity, and coherence:\n{content}"
    return generate_response(prompt)
