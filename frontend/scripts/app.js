document.addEventListener('DOMContentLoaded', () => {
    const boardsubmitbutton = document.getElementById("board-submit");
    if (boardsubmitbutton) {
        boardsubmitbutton.addEventListener('click', async function (event) {
            event.preventDefault();
            console.log('button clicked');
            const title = document.getElementById("title").value;
            const author_id= await getLoginUserId()
            console.log(author_id)

            // // Validate author_id
            // if (isNaN(author_id)) {
            //     alert("Invalid user ID");
            //     return;
            // }

            try {
                const response = await fetch(`http://localhost:8000/api/board?user_id=${author_id}`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        board_name: title,
                    }),
                    mode: 'cors',
                });

                if (response.ok) {
                    alert("Created successful!");
                    const data = await response.json();
                    const CreatedBoardId = data.board_id;
                    window.location.href = `board.html?boardid=${CreatedBoardId}`;
                } else {
                    alert("Error creating board");
                }

            } catch (err) {
                console.error('error:', err);
                alert("Error creating board");
            }
        });
    }

    const postitsubmitbutton= document.getElementById("postitsubmit");
    if (postitsubmitbutton) {
        postitsubmitbutton.addEventListener('click', async function (event) {
            event.preventDefault();
            const address=document.getElementById('address').value;
            const content=document.getElementById('content').value;
            const author=await getLoginUserId()
            const url=new URLSearchParams(window.location.search);
            const BoardId=url.get('boardid');


            try {
                const response=await fetch(`http://localhost:8000/api/board/${BoardId}/postit?user_id=${author}`,{
                    method: 'POST',
                    headers:{
                        'content-type': 'application/json',
                    },
                    body: JSON.stringify({
                        address:address,
                        content: content,

                    }),
                    mode:'cors',
                });

                if (response.ok) {
                    alert("Created successful!");
                    window.location.href =` board.html?boardid=${BoardId}`;
                }
            }
            catch (err){
                console.error('error:', err);
            }
        })
    }

    const BoardButton = document.getElementById("board-button");
    if (BoardButton) {
        BoardButton.addEventListener('click', async function (event) {
            // event.preventDefault();
            // const
            localStorage.setItem("boardtype","AllBoard")
            window.location.href = `boards.html`;

        })
    }

    const followiguserbutton = document.getElementById("following");
    if (followiguserbutton) {
        followiguserbutton.addEventListener('click', async function (event) {
            event.preventDefault();
            const url = new URLSearchParams(window.location.search);
            const targetuserid = url.get('userid');

            if (targetuserid) {
                localStorage.setItem("ListType", "following")
                window.location.href = `userList.html?userid=${targetuserid}`;
            }

        })
    }

    const followerbutton = document.getElementById("follower");
    if (followerbutton) {
        followerbutton.addEventListener('click', async function (event) {
            event.preventDefault();
            const url = new URLSearchParams(window.location.search);
            const targetuserid = url.get('userid');
            if (targetuserid) {
                localStorage.setItem("ListType", "follower")
                window.location.href = `userList.html?userid=${targetuserid}`;
            }
        })
    }

    const followbutton = document.getElementById("follow-button");

    if (followbutton) {
        followbutton.addEventListener('click', async function (event) {
            event.preventDefault(); // Prevent default action (optional)

            const MyId = await getLoginUserId();
            const url = new URLSearchParams(window.location.search);
            const UserId = url.get('userid');

            const response1 = await fetch(`http://localhost:8000/api/user/${UserId}/follower`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
                mode: 'cors',
            });

            if (response1.ok) {
                const followerlist = await response1.json();
                let isNotFollowing = true;

                for (const follower of followerlist) {
                    if (follower.id === MyId) {
                        isNotFollowing = false;
                        break;
                    }
                }

                if (isNotFollowing) {
                    const response2 = await fetch(`http://localhost:8000/api/user/${UserId}/follow?follower_id=${MyId}`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                    });

                    if (response2.ok) {
                        alert('Follow successful!');
                        window.location.reload();
                    } else {
                        alert('Error following user');
                    }
                } else {
                    alert('Already following');
                }
            } else {
                alert('Error fetching followers');
            }
        });
    }

    const UserBoardButton = document.getElementById('boards')

    if (UserBoardButton) {
        UserBoardButton.addEventListener('click', async function (event) {
            event.preventDefault();
            console.log('button click')
            const url=new URLSearchParams(window.location.search);
            const targetuserid = url.get('userid');
            localStorage.setItem('boardtype','UserBoard')
            window.location.href = `boards.html?userid=${targetuserid}`;
        })
    }

    const PostItListButton = document.getElementById('PostitList');
    if (PostItListButton) {
        PostItListButton.addEventListener('click', async function (event) {
            event.preventDefault();
            const MyId = await getLoginUserId();
            localStorage.setItem('postittype', 'UserPostit');
            window.location.href=`board.html?userid=${MyId}`;
        })
    }





    // const StarButton=document.getElementById("star-button")
    // if (StarButton) {
    //     StarButton.addEventListener('click', async function (event) {
    //         event.preventDefault();
    //         const
    //     })
    //
    // }

});

// star.js

// 즐겨찾기 등록 함수 (해제 기능 제거)
// async function AddStar(BoardID) {
//     try {
//         const MyId = await getLoginUserId(); // getLoginUserId는 이미 다른 파일에 존재하는 함수
//         const response = await fetch(`http://localhost:8000/api/board/${BoardID}/star?user_id=${MyId}`, {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             mode: "cors",
//         });
//
//         if (response.ok) {
//             const result = await response.json();
//             console.log(result); // 서버에서 응답 확인 (성공/실패 여부)
//
//             // UI 업데이트 (즐겨찾기 등록 후 버튼 아이콘을 변경)
//             const starButton = document.getElementById(`star-${BoardID}`).querySelector('i');
//             starButton.classList.remove('bi-star');
//             starButton.classList.add('bi-star-fill');
//         } else {
//             console.error('Failed to add star:', response.status);
//         }
//     } catch (error) {
//         console.error('Error adding star:', error);
//     }
// }
