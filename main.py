from research import research_topic
from utils import create_outline,generate_blog,optimize_seo,review_content
from saveblog import save_blog

#  main method get the input from the user and execute the method 
def main():
    topic = input("Enter your blog topic: ").strip()
    if not topic:
        print(" Error: Topic cannot be empty!")
        return

    research = research_topic(topic)
    outline = create_outline(topic)
    content = generate_blog(topic, outline)
    seo_content = optimize_seo(content)
    final_content = review_content(seo_content)

    save_blog(topic, final_content)
    print(f"🎉 Blog generated successfully! Files saved in 'blogs/{topic.lower().replace(' ', '_')}'")

if __name__ == "__main__":
    main()