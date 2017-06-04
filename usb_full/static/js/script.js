function send_root(text){
	$.ajax({
		type: 'POST',
		url:"/",
		contentType:'application/json;charset=UTF-8',
		dataType:'json',
		data: JSON.stringify({'ping':text}),
		success: function(response){
			transferred = response['pong'];
			console.log(transferred);
		},
		error: function(error){
			console.log(error);
		}
	});
}