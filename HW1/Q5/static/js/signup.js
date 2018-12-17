$(function() {				
	$('button').click(function(){
		var email_var = $('#useremail').val();
		var password_var = $('#userpassword').val();
	

		$.ajax({
			url: '/regis_process',
			data: {"email": email_var ,"password": password_var},
			type: 'POST',
			success: function(response){
			
				
				document.getElementById("check_pwd").innerHTML = "";
				
				if(response.status == true) {
					document.getElementById("check_pwd").innerHTML = "Congratulations on registering for CSE6242, " + response.email_data + "! Redirecting you to the course homepage...";
					$('#useremail').val("");
					$('#userpassword').val("");
					setTimeout(function(){window.location.href = 'http://poloclub.gatech.edu/cse6242/';}, 3000);
				}
				else{
					document.getElementById("check_pwd").innerHTML = response.email_data  + ",the password is invalid because it, ";
					
					if( response.password_data.includes(1) )
						document.getElementById("check_pwd").innerHTML += "1. Should be at least 8 characters in length";
					if( response.password_data.includes(3) )
						document.getElementById("check_pwd").innerHTML += "2. Should have at least 1 uppercase character";
					if( response.password_data.includes(2) ) 
						document.getElementById("check_pwd").innerHTML += "3. Should have at least 1 number";
					
					document.getElementById("check_pwd").innerHTML += ". Please try again!";
					$('#userpassword').val("");
				    
                }
				
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});