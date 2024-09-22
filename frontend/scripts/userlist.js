async function getUserList() {
    const url = new URLSearchParams(window.location.search);
    const userid = url.get('userid');
    if (localStorage.getItem("ListType") === "following") {
        try {
            const response = await fetch(`http://localhost:8000/api/user/${userid}/following`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
                mode: 'cors',
            });
            if (response.ok) {
                const users = await response.json();
                const userlist = document.getElementById("user-postit-container");
                users.forEach(user => {
                    const postit = document.createElement("div");
                    postit.className = "postit";
                    postit.innerHTML = `
                        <div class="postit-content">
                            <a href="userpage.html?userid=${user.id}">${user.nickname}</a>
                            <p>follower:${user.follower}</p>
                            <p>follower:${user.following}</p>
                        </div>
                    `;
                    userlist.appendChild(postit);
                });
            }
        } catch (error) {
            console.log(error);
        }
    }
    else{
        try{
            const response = await fetch(`http://localhost:8000/api/user/${userid}/follower`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
                mode: 'cors',
            });
            console.log(response)
            if (response.ok) {
                const users = await response.json();
                const userlist = document.getElementById("user-postit-container");
                users.forEach(user => {
                    const postit = document.createElement("div");
                    postit.className = "postit";
                    postit.innerHTML = `
                        <div class="postit-content">
                            <a href="userpage.html?userid=${user.id}">${user.nickname}</a>
                            <p>follower:${user.follower}</p>
                            <p>follower:${user.following}</p>
                        </div>
                    `;
                    userlist.appendChild(postit);
                });
            }
        } catch (error) {
            console.log(error);
        }
    }

}

window.onload = getUserList;
