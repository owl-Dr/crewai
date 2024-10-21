from crewai import Tool

def file_writer_tool(content: str, filename: str):
    """
    Write content to a file.

    Parameters:
    - content: The content to be written to the file.
    - filename: The name of the file to write to.

    Returns:
    - str: Confirmation message of the file writing operation.
    """
    with open(filename, 'w') as file:
        file.write(content)
    return f"Content successfully written to {filename}"

def format_post_tool(post: str, tone: str):
    """
    Format the social media post based on the specified tone.

    Parameters:
    - post: The raw social media post content.
    - tone: The desired tone for the post.

    Returns:
    - str: Formatted post according to the specified tone.
    """
    # Example formatting based on tone
    if tone == "professional":
        return f"***{post}***\n\n---\n*This post is brought to you by [Your Company Name].*"
    elif tone == "casual":
        return f"Hey everyone! 🌟\n\n{post}\n\nCheers! 🥳"
    elif tone == "humorous":
        return f"LOL! 😂\n\n{post}\n\nStay funny! 🎉"
    else:
        return post  # Default to no formatting

def generate_resources_tool(topic: str):
    """
    Generate resources based on the given topic.

    Parameters:
    - topic: The topic for which to generate resources.

    Returns:
    - list: A list of resources related to the topic.
    """
    # Sample implementation: This could be enhanced with real data fetching or generation logic
    resources = [
        f"Article on {topic} - A Comprehensive Guide",
        f"Video tutorial about {topic}",
        f"Infographic summarizing key points about {topic}",
    ]
    return resources

def write_post_tool(draft: str, tone: str):
    """
    Prepare a social media post based on the draft and tone.

    Parameters:
    - draft: The draft content of the post.
    - tone: The desired tone for the post.

    Returns:
    - str: The final version of the social media post.
    """
    formatted_post = format_post_tool(draft, tone)
    return formatted_post

# Additional tools can be defined here if necessary
