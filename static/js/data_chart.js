var myChart = function (id, data) {
  newData = getBirthdayData(data)
  categories= []
  for(var key in data){
    categories.push(key.substr(0,3))
    console.log(key)
  }
  Highcharts.chart(id, {
       chart: {
           type: 'column'
       },
       title: {
           text: 'Friend\'s Birthday'
       },
       xAxis: {
           title: {
               text: 'Birthday Month'
           },
           categories:categories
           // ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
           //    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
       },
       yAxis: {
           title: {
               text: 'No of Friends'
           }
       },
       series: [
         {
           name:"Birthday Count",
           // data
           data:newData,
         }
       ]
   });
};

var occupationChart = function (id, data) {
  Highcharts.chart(id, {
       chart: {
           type: 'pie'
       },
       title: {
           text: 'Friend\'s Occupation'
       },
       xAxis: {
           // title: {
           //     text: 'Birthday Month'
           // },
           categories: []
       },
       yAxis: {
           // title: {
           //     text: 'No of Friends'
           // }
       },
       series: [
         {
           name:"No of Friends",

           // data
           data:[{
             name:"Businessman",
             y:data['businessman']
           },
           {
             name:"Private_job",
             y:data['private_job']
           },
           {
             name:"Goverment Job",
             y:data['gov_job']
           }
         ],
       }
     ]
   });
};

function getBirthdayData(data) {
  newData = []
  // console.log(data)
  for(var key in data) {
    obj = {}
    obj['name'] = key
    obj['y'] = data[key]
    newData.push(obj)
  }
  console.log(newData)
  return newData
}
// {'January': 5, 'December': 4}
