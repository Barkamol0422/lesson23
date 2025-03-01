student_data={"id1":
{"name":"Sara",
"grade": "V",
"subjects":["biology","math"]},
"id2":
{"name":"Sara",
"grade": "V",
"subjects":["biology","math"]},
"id3":
{"name":"Sara",
"grade": "V",
"subjects":["biology","math"]},
"id4":
{"name":"Sara",
"grade": "V",
"subjects":["biology","math"]}
}
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)
