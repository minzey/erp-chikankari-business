/**
 * Created by Swati on 03-07-2016.
 */

$("#searchInput").keyup(function () {
    //split the current value of searchInput
    var data = this.value.toUpperCase().split(" ");
    //create a jquery object of the rows
    var jo = $("#klist").find("tr");
    if (this.value == "") {
        jo.show();
        return;
    }
    //hide all the rows
    jo.hide();

    //Recusively filter the jquery object to get results.
    jo.filter(function (i, v) {
        var $t = $(this);
        for (var d = 0; d < data.length; ++d) {
            if ($t.text().toUpperCase().indexOf(data[d]) > -1) {
                return true;
            }
        }
        return false;
    })
    //show the rows that match.
    .show();
}).focus(function () {
    this.value = "";
    $(this).css({
        "color": "black"
    });
    $(this).unbind('focus');
}).css({
    "color": "#C0C0C0"
});



//Karigar-wise overview
var table = $('#table_all_products').DataTable({
            aaSorting: [],
            bDestroy: true,
            dom: 'Bfrtip',
            buttons: [
            'copy', 'excel', 'print'
        ]
});
var issuetable = $('#table_product_issue').DataTable({bFilter: false, bInfo: false, bLengthChange: false, "aaSorting": [[1,'desc'], [0,'asc']]});
var receivetable = $('#table_product_receive').DataTable({bFilter: false, bInfo: false, bLengthChange: false,"aaSorting": [[1,'desc'], [0,'asc']]});
var reissuetable = $('#table_product_reissue').DataTable({bFilter: false, bInfo: false, bLengthChange: false,"aaSorting": [[1,'desc'], [0,'asc']]});

//Product-wise overview
var ktable = $('#table_all_karigars').DataTable({
            aaSorting: [],
            bDestroy: true,
            dom: 'Bfrtip',
            buttons: [
            'copy', 'excel', 'print'
        ]
});
var kissuetable = $('#table_karigar_issue').DataTable({bFilter: false, bInfo: false, bLengthChange: false,"aaSorting": [[1,'desc'], [0,'asc']]});
var kreceivetable = $('#table_karigar_receive').DataTable({bFilter: false, bInfo: false, bLengthChange: false,"aaSorting": [[1,'desc'], [0,'asc']]});
var kreissuetable = $('#table_karigar_reissue').DataTable({bFilter: false, bInfo: false, bLengthChange: false,"aaSorting": [[1,'desc'], [0,'asc']]});
var ktablesummary = $('#table_all_karigars_summary').DataTable({
    "bPaginate": false,
    "bLengthChange": false,
    "bFilter": true,
    "bInfo": false,
    "bSort": false
});

//Challan-wise overview
var ctable = $('#table_transactions').DataTable({
    aaSorting:[]
});

var dtable = $('#table_bar_selected').DataTable({
    aaSorting:[]
});

google.charts.load('current', {'packages':['bar']});


$(document).ready(function() {

    var loc = window.location.href; // returns the full URL
    if(/karigars_all/.test(loc)) {
        $('.nav.navbar-nav li #karigar').addClass('active');
    }

    $(".nav.navbar-nav li").click(function () {
            var id = $(this).attr("id");

            $('#' + id).siblings().find(".active").removeClass("active");
            $('#' + id).addClass("active");
            localStorage.setItem("selectedolditem", id);
        });

        var selectedolditem = localStorage.getItem('selectedolditem');

        if (selectedolditem != null) {
            $('#' + selectedolditem).siblings().find(".active").removeClass("active");
            $('#' + selectedolditem).addClass("active");
        }
    $("#goto_overview_from_assign").click(function () {
        console.log("button clicked");
        myname = $(this).data('karigarname');
        console.log(myname);
        console.log(document.getElementById("id_klist"));
        localStorage.setItem("karigar_select_index",myname);
    });


    $('#generate_report_btn').click(function () {
        console.log("button pressed");
        var start = document.getElementById('start_date').value;
        var end = document.getElementById('end_date').value;
        console.log("from = "+start+ typeof start);
        console.log("to = "+end+ typeof end);
       $.ajax({
           url : "get_report",
           type: 'get',
           dataType : 'json',
           data : {
               start_date: start,
               end_date : end
           },
           success: function(json){
               console.log(json);


               google.charts.setOnLoadCallback(drawChart);
                function drawChart() {
                    var rowcount=0;
                    var data = new google.visualization.DataTable();
                    data.addColumn('string', 'Product');
                    data.addColumn('number', 'stitch');
                    data.addColumn('number', 'block');
                    data.addColumn('number', 'emb');
                    data.addColumn('number', 'wash');
                    data.addColumn('number', 'addon');
                    console.log(json.length);
                    for(var i=0; i<json.length; ){
                        obj = json[i];
                        var nstitch=0, nblock=0, nemb=0, nwash=0, naddon=0;
                        var current_product = obj['product'];

                        var subproduct = obj['product'];

                        while(subproduct == current_product){
                            var received = json[i]['sum_received'] - json[i]['sum_reissued'];

                            switch (json[i]['karigar__profile']){
                                case 'stitch': nstitch = received; break;
                                case 'block' : nblock = received; break;
                                case 'emb' : nemb = received; break;
                                case 'wash' : nwash = received; break;
                                case 'addon' : naddon = received; break;
                            }
                            i=i+1;
                            if(i<json.length) {
                                obj = json[i];

                                subproduct = obj['product'];

                            }
                            else{
                                break;
                            }
                        }

                        data.addRow([current_product, nstitch, nblock, nemb, nwash, naddon]);
                        rowcount+=1;
                    }

                    console.log("Number of rows = "+data.getNumberOfRows());
                    var chartAreaHeight = rowcount * 150;
                    var chartHeight = chartAreaHeight + 80;
                    var options = {
                        height: chartAreaHeight, width: 1200,
                        chart: {
                            title: 'Performance Report',
                            subtitle: 'Process-wise progress of products'
                            
                        },
                        bars: 'horizontal' // Required for Material Bar Charts.

                    };

                    var chart = new google.charts.Bar(document.getElementById('barchart_material'));
                    google.visualization.events.addListener(chart, 'select', function () {
                        var selection = chart.getSelection();
                        if (selection.length) {
                            var row = selection[0].row;
                            var col = selection[0].column;
                            //console.log("row: "+row+" col: "+col);
                            //console.log("Product: "+data.getValue(row,0));
                            var productname = data.getValue(row,0);
                            var process;
                            switch (col){
                                case 1: process = 'stitch'; break;
                                case 2: process = 'block'; break;
                                case 3: process = 'emb'; break;
                                case 4: process = 'wash'; break;
                                case 5: process = 'addon'; break;
                            }
                            console.log(productname+process);
                            $.ajax({
                                url: 'get_report_table',
                                type: "get",
                                dataType: 'json',
                                data: {
                                    product: productname,
                                    process: process,
                                    start_date: start,
                                    end_date: end
                                },
                                success: function(json){
                                    console.log(json);
                                    dtable.clear().draw();

                                    for (var i = 0; i < json.length; i++) {
                                    //console.log("adding "+ json[i]);
    
                                        dtable.row.add([json[i].fields['challanid'], json[i].fields['assignmentdate'], json[i].fields['process'],
                                            json[i].fields['karigar'], json[i].fields['product'], json[i].fields['qty']]).draw();
                                    }
                                }
                            })

                        }
                    });
                    chart.draw(data, options);
                }
           }
       });
    });
    

    $('#id_klist').change(function () {

        var value;
        console.log("change called");
        if(localStorage.getItem("karigar_select_index") != null){
            value = localStorage.getItem("karigar_select_index");
            $('#id_klist').val(value);

            localStorage.removeItem("karigar_select_index");
        }
        else {
            //console.log(event.data.select_bydefault);
            var e = document.getElementById("id_klist");
            //console.log(e);
            //console.log(e.selectedIndex);
            value = e.options[e.selectedIndex].value;
        }
        $('#id_klist.chosen-select').trigger('chosen:updated');


        console.log(value);
        $.ajax({
                        url : "get_table_karigar",
                        type : "get",
                        dataType: 'json',
                        data : {
                            karigar_name : value,
                            csrfmiddlewaretoken: '{{ csrf_token }}'
                            },
                        success : function(json) {
                            console.log("length of json received: "+json.length);

                            var tr;
                            table.clear().draw();

                            issuetable.clear().draw();
                            receivetable.clear().draw();
                            reissuetable.clear().draw();

                            for (var i = 0; i < json.length; i++) {

                                // console.log("adding row to main table"+json[i].product+' '+json[i]['size']);
                                // console.log(json[i]['size']);
                                table.row.add([json[i].product,json[i]['size'], json[i].total_issued,
                                    json[i].total_received, json[i].pending]).draw();


                            }

                            table.$('tr.selected').removeClass('selected');

                            $("#all_products").unbind();
                            $('#all_products').on( 'click', 'tr', function (e) {

                                if ( $(this).hasClass('selected') ) {
                                    $(this).removeClass('selected');
                                }
                                else {
                                    $("#all_products").find('tr.selected').removeClass('selected');
                                    $(this).addClass('selected');
                                }
                                product_selected = table.row( this ).data()[0];
                                size_selected = table.row(this).data()[1];
                                console.log( "selected product: "+ table.row( this ).data()[0] );
                                console.log("selected size: "+size_selected);
                                issuetable.clear().draw();
                                receivetable.clear().draw();
                                reissuetable.clear().draw();
                                console.log("length json inside click: "+json.length);
                                for(var i = 0; i<json.length; i++){
                                    //console.log(i+" "+ json[i]);
                                    if (json[i].product == product_selected && json[i].size == size_selected){
                                        console.log("object found in ");
                                        console.log(json[i]);
                                        if(json[i].issue_transactions != 'No transactions') {
                                            obj = $.parseJSON(json[i].issue_transactions);
                                            //console.log("parsed json issue transs");
                                            //console.log(obj);

                                            for (var j = 0; j < obj.length; j++) {
                                                issuetable.row.add([obj[j].fields.challanid,
                                                    obj[j].fields.assignmentdate, obj[j].fields.qty]).draw()
                                            }

                                        }

                                        if(json[i].receive_transactions != 'No transactions') {
                                            obj = $.parseJSON(json[i].receive_transactions);
                                            //console.log("parsed json receive transs");
                                            //console.log(obj);

                                            for (var j = 0; j < obj.length; j++) {
                                                receivetable.row.add([obj[j].fields.challanid,
                                                    obj[j].fields.assignmentdate, obj[j].fields.qty]).draw()
                                            }

                                        }

                                        if(json[i].reissue_transactions != 'No transactions') {
                                            obj = $.parseJSON(json[i].reissue_transactions);
                                            //console.log("parsed json reissue transs");
                                            //console.log(obj);

                                            for (var j = 0; j < obj.length; j++) {
                                                reissuetable.row.add([obj[j].fields.challanid,
                                                    obj[j].fields.assignmentdate, obj[j].fields.qty]).draw()
                                            }

                                        }
                                    }
                                }

                            } );
                        },
                        error : function(xhr,errmsg,err) {
                            alert(xhr.status + ": " + xhr.responseText);
                        }
                    });
                    return false;
    });
    
    
    $('#id_plist').change(function () {
        var p = document.getElementById("id_plist");
        var value = p.options[p.selectedIndex].value;
        
        $('#id_plist.chosen-select').trigger('chosen:updated');
        console.log(value);
        $.ajax({
                        url : "get_table_product",
                        type : "get",
                        dataType: 'json',
                        data : {
                            product_id : value,
                            csrfmiddlewaretoken: '{{ csrf_token }}'
                            },
                        success : function(json) {
                            console.log("length of json received: "+json.length);

                            var tr;
                            ktable.clear().draw();
                            ktablesummary.clear().draw();
                            kissuetable.clear().draw();
                            kreceivetable.clear().draw();
                            kreissuetable.clear().draw();

                            for (var i = 0; i < json.length; i++) {
                                console.log("adding row to main table");
                                ktable.row.add([json[i].karigar, json[i].profile, json[i].total_issued,
                                    json[i].total_received, json[i].pending]).draw();


                            }

                            var stitchi=0, stitchr=0, blocki=0, blockr=0, embi=0, embr=0, washi=0, washr=0, addoni=0, addonr=0;
                            for(var j=0; j< json.length; j++){
                                if(json[j].profile == 'stitch') {
                                    stitchi += json[j].total_issued;
                                    stitchr += json[j].total_received;
                                }
                                else if(json[j].profile == 'block'){
                                    blocki += json[j].total_issued;
                                    blockr += json[j].total_received;
                                }
                                else if(json[j].profile == 'emb'){
                                    embi += json[j].total_issued;
                                    embr += json[j].total_received;
                                }
                                else if(json[j].profile == 'wash'){
                                    washi += json[j].total_issued;
                                    washr += json[j].total_received;
                                }
                                else if(json[j].profile == 'addon'){
                                    addoni += json[j].total_issued;
                                    addonr += json[j].total_received;
                                }
                            }

                            ktablesummary.row.add(['Stitch', stitchi, stitchr, stitchi-stitchr]).draw();
                            ktablesummary.row.add(['Block', blocki, blockr, blocki-blockr]).draw();
                            ktablesummary.row.add(['Emb', embi, embr, embi-embr]).draw();
                            ktablesummary.row.add(['Wash', washi, washr, washi-washr]).draw();
                            ktablesummary.row.add(['Addon', addoni, addonr, addoni-addonr]).draw();


                            ktable.$('tr.selected').removeClass('selected');

                            $("#all_karigars").unbind();
                            $('#all_karigars').on( 'click', 'tr', function (e) {

                                if ( $(this).hasClass('selected') ) {
                                    $(this).removeClass('selected');
                                }
                                else {
                                    $("#all_karigars").find('tr.selected').removeClass('selected');
                                    $(this).addClass('selected');
                                }
                                karigar_selected = ktable.row( this ).data()[0];
                                console.log( "selected karigar: "+ ktable.row( this ).data()[0] );
                                kissuetable.clear().draw();
                                kreceivetable.clear().draw();
                                kreissuetable.clear().draw();
                                console.log("length json inside click: "+json.length);
                                for(var i = 0; i<json.length; i++){
                                    console.log(i+" "+ json[i]);
                                    if (json[i].karigar == karigar_selected){
                                        console.log("object found in ");
                                        console.log(json[i]);
                                        if(json[i].issue_transactions != 'No transactions') {
                                            obj = $.parseJSON(json[i].issue_transactions);
                                            console.log("parsed json issue transs");
                                            console.log(obj);

                                            for (var j = 0; j < obj.length; j++) {
                                                kissuetable.row.add([obj[j].fields.challanid,
                                                    obj[j].fields.assignmentdate, obj[j].fields.qty]).draw()
                                            }

                                        }

                                        if(json[i].receive_transactions != 'No transactions') {
                                            obj = $.parseJSON(json[i].receive_transactions);
                                            console.log("parsed json receive transs");
                                            console.log(obj);

                                            for (var j = 0; j < obj.length; j++) {
                                                kreceivetable.row.add([obj[j].fields.challanid,
                                                    obj[j].fields.assignmentdate, obj[j].fields.qty]).draw()
                                            }

                                        }

                                        if(json[i].reissue_transactions != 'No transactions') {
                                            obj = $.parseJSON(json[i].reissue_transactions);
                                            console.log("parsed json reissue transs");
                                            console.log(obj);

                                            for (var j = 0; j < obj.length; j++) {
                                                kreissuetable.row.add([obj[j].fields.challanid,
                                                    obj[j].fields.assignmentdate, obj[j].fields.qty]).draw()
                                            }

                                        }
                                    }
                                }

                            } );
                        },
                        error : function(xhr,errmsg,err) {
                            alert(xhr.status + ": " + xhr.responseText);
                        }
                    });
                    return false;

    });
    
    $('#id_clist').change(function () {
        var p = document.getElementById("id_clist");
        var value = p.options[p.selectedIndex].value;
        var challan_selected = null;
        $('#id_clist.chosen-select').trigger('chosen:updated');
        $.ajax({
                        url : "get_table_challan",
                        type : "get",
                        dataType: 'json',
                        data : {
                            challan_id : value,
                            csrfmiddlewaretoken: '{{ csrf_token }}'
                            },
                        success : function(json) {
                            console.log("length of json received: "+json.length);
                            console.log(json);
                            ctable.column(7).visible(false);
                            ctable.clear().draw();

                            for (var i = 0; i < json.length; i++) {
                                //console.log("adding "+ json[i]);

                                ctable.row.add([json[i].fields['challanid'], json[i].fields['assignmentdate'], json[i].fields['process'],
                                    json[i].fields['karigar'], json[i].fields['product'], json[i].fields['size'], 
                                    json[i].fields['qty'], json[i].pk]).draw();
                            }
                            $('#transactions').unbind();
                            $('#transactions').on( 'click', 'tr', function (e) {

                                if ($(this).hasClass('selected')) {
                                    $(this).removeClass('selected');
                                    challan_selected=null;
                                    document.getElementById("edit_btn").href= "";
                                }
                                else {
                                    $('#transactions').find('tr.selected').removeClass('selected');
                                    $(this).addClass('selected');
                                    challan_selected = ctable.row(this).data();
                                    document.getElementById("edit_btn").href= "edit_assignment/"+challan_selected[7];
                                }

                                
                            });
                            
                            $('#delete_btn').unbind();
                            $('#delete_btn').on('click', function(e){

                                if (challan_selected !=null)
                                $.ajax({
                                    url: "delete_assignment",
                                    dataType : 'json',
                                    type: "get",
                                    data:{
                                        challan_id : challan_selected[0],
                                        karigar : challan_selected[3],
                                        product : challan_selected[4],
                                        size: challan_selected[5],
                                        qty : challan_selected[6],
                                        csrfmiddlewaretoken: '{{ csrf_token }}'
                                    },
                                    success: function(response){
                                        console.log(response);
                                        alert("Deleted successfully:\n"+response[0].fields['challanid']+"\n"+response[0].fields['assignmentdate']+"\n"+
                                        response[0].fields['karigar']+"\n"+response[0].fields['process']+
                                        "\n"+response[0].fields['product']+"\n"+response[0].fields['qty']+"\n"+response[0].fields['size']);

                                        ctable.row('.selected').remove().draw( false );
                                    }
                                });
                                return false;
                            });                            
                        },
                        error : function(xhr,errmsg,err) {
                            alert(xhr.status + ": " + xhr.responseText);
                        }
        });
        return false;
               
    });


   
    console.log("my dom is ready");
    //console.log(document.getElementById('id_plist'));
    $('#id_plist.chosen-select').chosen({
    no_results_text: "No product found!",
    width: "98%"});
    
    $('#id_klist.chosen-select').chosen({
    no_results_text: "No karigar found!",
    width: "98%"});
    
    $('#id_clist.chosen-select').chosen({
    no_results_text: "No challan found!",
    width: "98%"});

    for(var i=0; i<=5; i++) {
        $('#id_form-' + i + '-product.form-control').chosen({
            no_results_text: "No product found!",
            width: "100%"
        });
    }
    
    $('#id_klist').change();
    $('#id_plist').change();
    $('#id_clist').change();

});




