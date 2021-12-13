from CandidateFinder.models import * 
skill1 = Skill(skill = "c++")  
skill2 = Skill(skill = "javascript")   
skill3 = Skill(skill = "react")
skill1.save()
skill2.save()
skill3.save()
candidate1= Candidate(name = "Arye Pr",title = "Amature programmer")
