# "Version"       : "1.1.17"
# "Last Updated"  : "23/09/2023"

if __name__ == "__AboutMe__":
  AboutMe()
# This is a self introduction in python block code
class AustinLai:
    def __init__(self):
        self.name = "Austin Lai"
        self.previous_role = ["Red Teamer (Offensive Security)", "CyberSecurity Engineer", "Network Engineer"]
        self.current_role = "Tech Tutor in QRC"
        self.skills = ["Python", "Docker", "Shell Script", "Home labs development"]
        self.interests = ["Phishing", "Build Hacker Toolsets and C2", "Malware development", "Web Application Security", "Penetration Testing"]
    
    def introduce(self):
        print(f"\nHi, I'm {self.name}, and I've been worked as {', '.join(self.previous_role)} for the past 6 years.\n")
        print(f"Some of the skills and topics that I have learned by myself are {', '.join(self.skills)}, {', '.join(self.interests)}.\n")
        print(f"Thank you for reading my introduction, and I hope to connect with you soon.\n")

me = AustinLai()

me.introduce()
