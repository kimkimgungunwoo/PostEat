async function getPostItList() {
    const postittype=localStorage.getItem('postittype');
    let postitUrl='';

    if(postittype==="common"){
        const url=new URLSearchParams(window.location.search);
        const BoardId=url.get('boardid')
        postitUrl=`http://localhost:8000/api/board/${BoardId}/postit`;
    }
    else if(postittype==="UserPostit"){
        const url=new URLSearchParams(window.location.search);
        const UserId=url.get("userid");
        postitUrl=`http://localhost:8000/api/user/${UserId}/postit`;
    }

    try{
        const response = await fetch(postitUrl, {
            method: 'GET',
            headers:{
                'Content-Type': 'application/json',
            },
            mode: "cors",
        });
        if (response.ok) {
            const Postits = await response.json();
            console.log(Postits);
            const PostitContainer = document.getElementById("postit-container");

            for (const PostitContent of Postits) {
                const postit=document.createElement("div");
                const AuthorId=PostitContent.user_id
                console.log(AuthorId)
                try{
                    const userResponse = await fetch(`http://localhost:8000/api/user/${AuthorId}`, {
                        method: 'GET',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        mode: 'cors',
                    });

                    const userData=await userResponse.json();
                    const username=userData.nickname;

                    if(userResponse.ok){
                        postit.className = "postit";
                        postit.innerHTML = `
                        
                        <div class="postit-content">    
                            <h2>${PostitContent.address}</h2>
                            <h4>${PostitContent.content}</h4>
                            <a href="userpage.html?userid=${AuthorId}">${username}</a>
                            <div class="like">  
                                <button type="button" id="like">    
                                    <i class="bi bi-heart"></i>
                                </button>
                            </div>
                        </div>
                        
                        
                        `;
                        PostitContainer.appendChild(postit);
                    }else{
                        console.error('Failed to fetch user data');
                    }

                }
                catch(error){
                    console.error('Error fetching user:', error);
                }

            }
        }else{console.error('Failed to fetch board list');
    }

    }catch(error){
        console.error('Error fetching postit list');
    }
}

window.onload=getPostItList;