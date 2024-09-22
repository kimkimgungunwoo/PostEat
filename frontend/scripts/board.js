async function getBoardList() {
    const boardtype = localStorage.getItem("boardtype");
    let boardUrl = '';

    if (boardtype === "AllBoard") {
        boardUrl = 'http://localhost:8000/api/board';
    } else if (boardtype === "UserBoard") {
        const url = new URLSearchParams(window.location.search);
        const UserId = url.get("userid");
        boardUrl = `http://localhost:8000/api/user/${UserId}/boards`;
    }
    else if (boardtype === "StarBoard") {
        const url = new URLSearchParams(window.location.search);
        const UserId = url.get("userid");
        boardUrl = `http://localhost:8000/api/user/${UserId}/star`;
    }

    try {
        const response = await fetch(boardUrl, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
            mode: "cors",
        });

        if (response.ok) {
            const boards = await response.json();
            const BoardContainer = document.getElementById("board-container");
            console.log(boards)
            for (const BoardContent of boards) {
                const board = document.createElement("div");
                const AuthorId = BoardContent.user_id;

                try {
                    const userResponse = await fetch(`http://localhost:8000/api/user/${AuthorId}`, {
                        method: 'GET',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        mode: 'cors',
                    });

                    const userData = await userResponse.json();
                    const username = userData.nickname;
                    localStorage.setItem('postittype', 'common');

                    if (userResponse.ok) {
                        board.className = "board";
                        board.innerHTML = `
                            <h2><a href="board.html?boardid=${BoardContent.board_id}">${BoardContent.board_name}</a></h2>
                            <h4><a href="userpage.html?userid=${BoardContent.user_id}">${username}</a></h4>
                            
                        `;
                        BoardContainer.appendChild(board);
                    } else {
                        console.error('Failed to fetch user data');
                    }
                } catch (error) {
                    console.error('Error fetching user:', error);
                }
            }
        } else {
            console.error('Failed to fetch board list');
        }
    } catch (error) {
        console.error('Error fetching board list:', error);
    }
}

window.onload = getBoardList;
