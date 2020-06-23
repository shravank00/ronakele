<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<!-- Mirrored from www.kunaimpex.com/process/TrecinLocator.php by HTTrack Website Copier/3.x [XR&CO'2014], Thu, 11 Jun 2020 11:20:19 GMT -->
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Untitled Document</title>
<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>

<script type="text/javascript">
	function initialize() {
		var latlng = new google.maps.LatLng(23.04108, 72.513738);
		var settings = {
			zoom:16,
			center: latlng,
			mapTypeControl: true,
			mapTypeControlOptions: {style: google.maps.MapTypeControlStyle.DROPDOWN_MENU},
			navigationControl: true,
			navigationControlOptions: {style: google.maps.NavigationControlStyle.SMALL},
			mapTypeId: google.maps.MapTypeId.ROADMAP
    };
	
	var map = new google.maps.Map(document.getElementById("map_canvas"), settings);

	var companyPos = new google.maps.LatLng(23.04108, 72.513738);
	var companyMarker = new google.maps.Marker({
	  position: companyPos,
	  map: map,
	  title:"Some title"
	});	

var contentString = '<div id="content" style="font-family:Book Antiqua;width:320px; height:80px;">'+
    '<div id="siteNotice">'+
    '</div>'+
    '<div id="bodyContent">'+
    '<p style="font-size:15px;text-align: center;"><b  style="color:#FF0708; font-size:14px; ">Kuna Impex Pvt. Ltd.</b><br>202,203, NAINDHARA, NEAR GNFC INFO TOWER, BODAKDEV AHMEDABAD-380 054. GUJARAT (INDIA)</b></p>'+
    '</div>'+
    '</div>';
 
var infowindow = new google.maps.InfoWindow({
    content: contentString
});
infowindow.open(map,companyMarker);
}
</script>	
</head>

<body onload="initialize()">
  <div id="map_canvas" style="width:100%; height:369px;"></div>
</body>

<!-- Mirrored from www.kunaimpex.com/process/TrecinLocator.php by HTTrack Website Copier/3.x [XR&CO'2014], Thu, 11 Jun 2020 11:20:19 GMT -->
</html>
