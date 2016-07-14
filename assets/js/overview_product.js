/**
 * Created by Swati on 08-07-2016.
 */
var ktable = $('#table_all_karigars').DataTable({
            aaSorting: [],
            bDestroy: true,
            dom: 'Bfrtip',
            buttons: [
            'copy', 'excel', 'print'
        ]
});
var kissuetable = $('#table_karigar_issue').DataTable({bFilter: false, bInfo: false});
var kreceivetable = $('#table_karigar_receive').DataTable({bFilter: false, bInfo: false});
var kreissuetable = $('#table_karigar_reissue').DataTable({bFilter: false, bInfo: false});

$(document).ready(function() {
    //var table = $('#table_all_products').DataTable({bDestroy: true});

    

    $('#id_plist').change(function () {
        var e = document.getElementById("id_plist");
        var value = e.options[e.selectedIndex].value;
        

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
                            kissuetable.clear().draw();
                            kreceivetable.clear().draw();
                            kreissuetable.clear().draw();

                            for (var i = 0; i < json.length; i++) {
                                console.log("adding row to main table");
                                ktable.row.add([json[i].karigar, json[i].profile, json[i].total_issued,
                                    json[i].total_received, json[i].pending]).draw();


                            }
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
                                console.log( "selected product: "+ ktable.row( this ).data()[0] );
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
});

