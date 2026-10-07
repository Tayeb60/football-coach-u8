# ============================================================
# PROMPT TEMPLATES FOR U8 FOOTBALL COACHING
# ============================================================

SYSTEM_PROMPT = """
You are an experienced FA-qualified youth football coach specialising in coaching children aged 6 to 8 (U8).

Your role is to help coaches design fun, safe, and age-appropriate training sessions and drills.

Your coaching philosophy:
- FUN is the number one priority. If the children are not enjoying it, they are not learning.
- Every child should be active and involved. No long queues or waiting.
- Use small-sided games (3v3 or 4v4) as much as possible.
- Focus on fundamental skills: dribbling, passing, shooting, movement, and spatial awareness.
- Use simple, clear language that a 7-year-old can understand.
- Positive reinforcement: praise effort, not just outcomes.
- Safety first: no heading, no slide tackling, no intense physical contact.
- Keep sessions short: 45-60 minutes maximum, with frequent water breaks.

When you design a drill or session, always include:
1. **Objective**: What skill or concept is being developed
2. **Setup**: How to set up the area, equipment, and players
3. **Instructions**: Simple, step-by-step instructions for the children
4. **Coaching Points**: Key things the coach should look for and say
5. **Variations**: How to make it easier or harder
6. **Duration**: How long the drill should last

Always use UK English and FA terminology.
"""

def get_drill_prompt(drill_description, language="English"):
    """Generate a prompt for creating a drill."""
    return f"""
A coach wants to create a training drill for U8 children.

Their description:
{drill_description}

Please design a complete, age-appropriate drill that:
- Is fun and game-based
- Keeps all children active
- Develops fundamental skills
- Is safe for 6-8 year olds
- Can be run in a small space with basic equipment

Provide the drill in {language}, using this exact format:

### Drill Name
[A short, fun name]

### Objective
[What skill or concept is being developed]

### Setup
[Area size, equipment needed, number of players]

### Instructions
[Simple step-by-step instructions for the children]

### Coaching Points
[Key things the coach should look for and say]

### Variations
- Easier: [How to make it simpler]
- Harder: [How to make it more challenging]

### Duration
[How long the drill should last]

### Safety Notes
[Any specific safety considerations for U8]
"""

def get_session_prompt(session_theme, duration_minutes=60, language="English"):
    """Generate a prompt for creating a full session plan."""
    return f"""
A coach wants to plan a complete U8 training session.

Session theme: {session_theme}
Total duration: {duration_minutes} minutes

Please design a complete session plan that:
- Is fun and game-based
- Keeps all children active
- Develops fundamental skills related to the theme
- Is safe for 6-8 year olds
- Follows a logical progression: warm-up, main activities, cool-down

Provide the session plan in {language}, using this exact format:

### Session Overview
[Theme, duration, number of players, equipment needed]

### Warm-Up (10 minutes)
[Fun, dynamic warm-up activity]

### Main Activity 1 (15 minutes)
[First skill-focused drill]

### Main Activity 2 (15 minutes)
[Second skill-focused drill, building on the first]

### Small-Sided Game (15 minutes)
[3v3 or 4v4 game with the session theme in mind]

### Cool-Down (5 minutes)
[Fun, relaxed activity to finish]

### Key Coaching Points for the Session
[3-5 key things to reinforce throughout]

### Equipment List
[Everything the coach needs to prepare]
"""