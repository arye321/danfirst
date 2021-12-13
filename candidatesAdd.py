candidate1= Candidate(name = "Daniel Pr",title = "Student at TA-Yafo college ")
candidate1.save()
candidate1.skills.add(Skill.objects.all()[0])
candidate1.save()