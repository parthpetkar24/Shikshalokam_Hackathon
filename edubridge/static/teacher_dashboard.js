    function submitIssue() {
        const btn = document.querySelector('#issueForm button');
        const response = document.getElementById('aiResponse');
        
        btn.innerText = "Analyzing...";
        
        // Simulate API call
        setTimeout(() => {
            btn.innerText = "Submitted";
            btn.classList.add('outline');
            btn.classList.remove('primary');
            response.style.display = 'block';
        }, 1500);
    }