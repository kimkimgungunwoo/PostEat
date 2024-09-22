
document.addEventListener('DOMContentLoaded', function() {

    const loginLogoutButton = document.getElementById('login-logout');
    if (loginLogoutButton) {
        loginLogoutButton.addEventListener('click', async function(event) {
            const token = localStorage.getItem('jwtToken');
            if (token) {
                localStorage.removeItem('jwtToken');
                alert("Logout successful!");
                window.location.href = 'boards.html';
            } else {
                window.location.href = 'login.html';
            }
        });
    }

    const loginButton = document.getElementById('loginButton');
    if (loginButton) {
        loginButton.addEventListener('click', async function(event) {
            event.preventDefault();

            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            const formData = new URLSearchParams();
            formData.append('username', email);
            formData.append('password', password);

            try {
                const response = await fetch('http://127.0.0.1:8000/api/user/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded'
                    },
                    body: formData,
                    mode: 'cors'
                });

                if (response.ok) {
                    const data = await response.json();
                    localStorage.setItem('jwtToken', data.access_token);
                    const loginuserid=await getLoginUserId();
                    window.location.href='userpage.html?userid=' + loginuserid;
                    console.log(localStorage.getItem('jwtToken'));
                } else {
                    alert("Login failed.");
                }
            } catch (error) {
                console.log("Error:", error);
                alert("Login failed.");
            }

            // const loginuserid=await fetch(
            //     'http://127.0.0.1:8000:api/user/me',{
            //         method: 'GET',
            //         headers:{
            //             'Authorization': 'Bearer ' + localStorage.getItem('jwtToken'),
            //         }
            //
            //     }
            // )
            // if (loginuserid.ok){
            //     localStorage.setItem('loginuserid',loginuserid);
            //     console.log(loginuserid);
            //
            // }
        });
    }

    const signupButton = document.getElementById('signup-button');
    if (signupButton) {
        signupButton.addEventListener('click', async function(event) {
            event.preventDefault();
            const email = document.getElementById('email').value;
            const password1 = document.getElementById('password1').value;
            const password2 = document.getElementById('password2').value;
            const nickname = document.getElementById('nickname').value;

            try {
                const response = await fetch('http://127.0.0.1:8000/api/user/signup', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        email: email,
                        password1: password1,
                        password2: password2,
                        nickname: nickname
                    }),
                    mode: "cors"
                });

                if (response.ok) {
                    alert("Signup successful!");
                    window.location.href = 'login.html';
                } else {
                    const errorData = await response.json();
                    console.log(errorData);
                    alert(`Signup failed: ${errorData.message}`);
                }
            } catch (error) {
                console.log("Error:", error);
                alert("Signup failed.");
            }

        });
    }
    const editbutton = document.getElementById('edit-button');
    if (editbutton) {
        editbutton.addEventListener('click', async function(event) {
            event.preventDefault();
            const token = localStorage.getItem('jwtToken');
            if (token) {
                if(editbutton.innerText==="Edit-postit"){
                    const url=new URLSearchParams(window.location.search);
                    const BoardId=url.get('boardid');
                    window.location.href = `postitform.html?boardid=${BoardId}`;
                }
                else{
                    window.location.href='postboard.html'
                }
            }
            else{
                window.location.href='login.html';
                alert('login please');
            }
        })
    }

    const mypagebutton = document.getElementById('mypage-button');
    if (mypagebutton) {
        mypagebutton.addEventListener('click', async function(event) {
            event.preventDefault();
            const token = localStorage.getItem('jwtToken');
            if (token) {
                const loginUserId = await getLoginUserId();
                if (loginUserId) {
                    window.location.href = `userpage.html?userid=${loginUserId}`;
                } else {
                    alert("Failed to retrieve user ID.");
                }
            } else {
                window.location.href = 'login.html';
                alert('login please');
            }
        });
    }
});

async function getLoginUserId() {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/user/me', {
            method: 'GET',
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem('jwtToken'),
            }
        });

        if (response.ok) {
            const data = await response.json();
            return data.user_id; // user_id 반환
        } else {
            console.log("Failed to fetch user information.");
            return null; // 실패 시 null 반환
        }
    } catch (error) {
        console.log("Error:", error);
        return null; // 에러 발생 시 null 반환
    }
}