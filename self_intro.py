# "Version"       : "3.0"
# "Last Updated"  : "23/05/2026"

class AustinLai:
    def __init__(self):
        self.name = "Austin Lai"
        self.previous_role = [
            "Red Teamer (Offensive Security)",
            "Security Engineer",
            "ICT - Cloud & Security Specialist"
        ]
        self.current_role = "SOC Analyst"
        self.skills = ["Python"]
        self.interests = [
            "Phishing simulation",
            "Building security toolkit",
            "Malware development research",
            "Web application security",
            "Penetration testing"
        ]

    def introduce(self):
        print(f"\nHi, I'm {self.name}. I've worked as {', '.join(self.previous_role)} for the past 6 years.\n")
        print(f"Some of the skills and topics I've explored include: {', '.join(self.skills)}, {', '.join(self.interests)}.\n")
        print("Thanks for reading my introduction. Looking forward to connecting.\n")


if __name__ == "__main__":
    me = AustinLai()
    me.introduce()
