// Disease Chart

new Chart(
document.getElementById("diseaseChart"),
{

type:"doughnut",

data:{

labels:diseaseLabels,

datasets:[{

label:"Disease Cases",

data:diseaseValues

}]

},

options:{

responsive:true

}

}

);





// Risk Chart


new Chart(
document.getElementById("riskChart"),
{

type:"bar",

data:{

labels:[

"High Risk",

"Low Risk"

],


datasets:[{

label:"Patients",

data:[

highRisk,

lowRisk

]

}]

},

options:{

responsive:true

}

}

);