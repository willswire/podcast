from pathlib import Path
import openai

conversation = [
    "Great! I'm Bob, your co-host for 'Hacker News Discussed.' Let's dive into today's lineup of news articles from Hacker News and break down what's happening in the tech world.",
    "This is indeed a fascinating development, Bob. It raises questions about the future of software engineering and how we might integrate AI into our workflows more seamlessly.",
    "Alright, this first article is a real eye-opener. We've seen AI making strides in various fields, but surpassing human performance in coding competitions is a significant milestone. Alice, what are your initial thoughts on this development?",
    "And there’s also the matter of trust and reliability. AI models are powerful, but they’re not infallible. How do we ensure the code generated is secure, efficient, and maintainable?",
    "Absolutely. On one hand, it’s impressive to see AI handling complex coding challenges, potentially increasing productivity and pushing the boundaries of what’s possible. On the other hand, it raises concerns about job displacement and the evolving role of software engineers. We need to consider how we can leverage AI as a tool rather than see it as a threat.",
    "Security breaches like this are always concerning, Bob. They highlight the vulnerabilities that exist even in well-established and trusted services. It’s a reminder that security needs to be a top priority at all times.",
    "Good point, Alice. AI can certainly assist in generating code, but the human element is crucial for reviewing and understanding the context in which that code will be used. It’s a partnership where both humans and AI have roles to play.",
    "And for the users, it’s a wake-up call to ensure they’re implementing best practices, such as using strong, unique passwords, enabling multi-factor authentication, and regularly updating their software.",
    "Now, onto the next article. A major security breach in a popular cloud service provider has been reported. This is a critical issue, especially given how many businesses rely on cloud infrastructure. Alice, what’s your take on this?",
    "Quantum computing is one of those fields that feels like science fiction, but it’s rapidly becoming science fact. This breakthrough could pave the way for solving problems that are currently intractable for classical computers.",
    "Indeed. It also underscores the importance of having robust incident response plans and regular security audits. Companies must stay vigilant and proactive in protecting their data and systems.",
    "Yes, and while it’s exciting, we need to manage our expectations. Practical, everyday applications of quantum computing might still be a few years away, but the progress we’re seeing is promising.",
    "Exactly. Security is a shared responsibility, and everyone from the service provider to the end-user has a role to play. It’s about creating a culture of security awareness and preparedness.",
    "That’s all for today’s episode of 'Hacker News Discussed.' We’ve covered some groundbreaking topics, and we’d love to hear your thoughts. Reach out to us on social media or leave a comment. Until next time, keep exploring and stay curious!",
    "Finally, let's talk about this breakthrough in quantum computing. The article claims we’re getting closer to practical applications of this technology. What do you think, Alice?",
    "It’s a thrilling time to be in tech, witnessing these advancements firsthand. Quantum computing has the potential to revolutionize many industries, and it’s crucial for us to stay informed and prepared for the changes it will bring."
]

for i in range(len(conversation)):
    voice = "nova" if (i % 2) else "onyx"
    speech_file_path = Path(__file__).parent / f"part_{i}.mp3"
    response = openai.audio.speech.create(
    model="tts-1-hd",
    speed="1.1"
    voice=voice,
    input=conversation[i]
    )
    response.stream_to_file(speech_file_path)
