//{title:"Evedence", field:"data",  formatter:"link", formatterParams:{target:"_blank"}},

var table = new Tabulator("#example-table", {
        ajaxURL: "api/index.json",
	layout:"fitDataStretch",
        pagination:"local",
        paginationSize:25,
        paginationSizeSelector:[50, 100, 500, 1000, 5000],
        movableColumns:true,
        columns:[
                {title:"IP", field:"ip", sorter:"string"},
                {title:"Data", field:"data"},
                ],
        ajaxResponse:function(url, params, response){return response.data;},
});

//trigger download of data.csv file
document.getElementById("download-csv").addEventListener("click", function(){
    table.download("csv", "index.csv");
});

//trigger download of data.pdf file
document.getElementById("download-pdf").addEventListener("click", function(){
    table.download("pdf", "index.pdf", {
        orientation:"portrait", //set page orientation to portrait
        title:"Example Report", //add title to report
    });
});
