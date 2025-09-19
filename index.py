"""
# Streamlit 앱으로 HTML 게임을 임베드합니다.
# - 모든 변수/함수는 snake_case 로 작성합니다.
# - 명확한 한국어 주석을 포함합니다.
"""

import streamlit as st
from streamlit.components.v1 import html as components_html


def load_game_html() -> str:
    """
    게임에 사용할 전체 HTML을 문자열로 반환합니다.
    - TailwindCDN과 Google Fonts를 사용합니다.
    - 기존 상호작용 로직(JS)을 그대로 유지합니다.
    """
    html_content = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>The Case of the Missing Cookies</title>
    <script src=\"https://cdn.tailwindcss.com\"></script>
    <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">
    <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>
    <link href=\"https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap\" rel=\"stylesheet\">
    <style>
        body {
            background: #2c3e50;
            color: #ecf0f1;
            font-family: 'Playfair Display', serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        .parchment-container {
            background-color: #f4f1e4;
            color: #4b4b4b;
            border: 5px solid #8b7d6b;
            padding: 2rem;
            max-width: 900px;
            width: 100%;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            text-align: center;
        }
        .question-box { background-color: #e0d7c7; padding: 1.5rem; border-radius: 8px; margin-top: 1.5rem; border: 2px dashed #a1978a; }
        .input-text { width: 100%; padding: 0.75rem; border-radius: 6px; border: 1px solid #ccc; margin-top: 0.5rem; font-family: 'Playfair Display', serif; color: #4b4b4b; }
        .btn { background-color: #c0392b; color: white; padding: 0.75rem 1.5rem; border-radius: 6px; transition: transform 0.2s, background-color 0.2s; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        .btn:hover { background-color: #e74c3c; transform: translateY(-2px); }
        .success { color: #27ae60; }
        .error { color: #c0392b; }
    </style>
</head>
<body class=\"bg-gray-900 text-white flex items-center justify-center min-h-screen p-6\">
    <div class=\"parchment-container\">
        <div id=\"game-container\">
            <div id=\"mission-intro\" class=\"mission-section\">
                <h1 class=\"text-4xl font-bold mb-4\">The Case of the Missing Cookies</h1>
                <p class=\"text-lg mb-6\">Welcome, junior detectives! ...</p>
                <button id=\"start-mission-btn\" class=\"btn text-xl font-bold\">Start Your Investigation</button>
            </div>
            <div id=\"mission-1\" class=\"mission-section hidden\">
                <h2 class=\"text-3xl font-bold mb-4\">Mission 1: The Suspects' Statements</h2>
                <div class=\"text-left mb-6 leading-relaxed\">
                    <div class=\"question-box\">
                        <p class=\"font-bold\">Tim, the delivery boy:</p>
                        <p class=\"italic\">\"I was delivering bread ... it wasn't me that took them!\"</p>
                    </div>
                    <div class=\"question-box mt-4\">
                        <p class=\"font-bold\">Lisa, the new cashier:</p>
                        <p class=\"italic\">\"I was cleaning ... It was the delivery boy that was standing near the cookies!\"</p>
                    </div>
                    <div class=\"question-box mt-4\">
                        <p class=\"font-bold\">Mr. Jones, a customer:</p>
                        <p class=\"italic\">\"I came in ... It was the new cashier that I saw putting something in her bag!\"</p>
                    </div>
                </div>
                <div class=\"question-box\">
                    <p class=\"font-bold\">Question 1: Who did Lisa say was standing near the cookies?</p>
                    <p class=\"mb-2\">Start your answer with \"It was... that...\"</p>
                    <input type=\"text\" id=\"q1-input\" class=\"input-text\" placeholder=\"It was... that...\">
                    <button id=\"submit-q1-btn\" class=\"btn mt-4 w-full\">Submit Answer</button>
                    <p id=\"q1-feedback\" class=\"feedback-message mt-2\"></p>
                </div>
            </div>
            <div id=\"mission-2\" class=\"mission-section hidden\">
                <h2 class=\"text-3xl font-bold mb-4\">Mission 2: Finding the Witness</h2>
                <p class=\"mb-4\">Mr. Jones saw something important. Use his statement to answer the next question.</p>
                <div class=\"question-box\">
                    <p class=\"font-bold\">Question 2: Who did Mr. Jones see putting something in her bag?</p>
                    <p class=\"mb-2\">Start your answer with \"It was... that...\"</p>
                    <input type=\"text\" id=\"q2-input\" class=\"input-text\" placeholder=\"It was... that...\">
                    <button id=\"submit-q2-btn\" class=\"btn mt-4 w-full\">Submit Answer</button>
                    <p id=\"q2-feedback\" class=\"feedback-message mt-2\"></p>
                </div>
            </div>
            <div id=\"mission-3\" class=\"mission-section hidden\">
                <h2 class=\"text-3xl font-bold mb-4\">Mission 3: The Biggest Clue</h2>
                <div class=\"question-box\">
                    <p class=\"font-bold\">Question 3: Read the story again. What is the biggest clue?</p>
                    <p class=\"mb-2\">Explain in a short sentence.</p>
                    <textarea id=\"q3-input\" class=\"input-text h-24\" placeholder=\"Think about where Lisa was and what she said she saw.\"></textarea>
                    <button id=\"submit-q3-btn\" class=\"btn mt-4 w-full\">Submit Answer</button>
                    <p id=\"q3-feedback\" class=\"feedback-message mt-2\"></p>
                </div>
            </div>
            <div id=\"mission-4\" class=\"mission-section hidden\">
                <h2 class=\"text-3xl font-bold mb-4\">Mission 4: The Final Reveal</h2>
                <div class=\"question-box\">
                    <p class=\"font-bold\">Question 4: So, who is the cookie thief? Why?</p>
                    <p class=\"mb-2\">Choose the thief and then use a sentence that starts with <strong>It was... that...</strong></p>
                    <select id=\"q4-suspect\" class=\"input-text\">
                        <option value=\"\">Choose the thief...</option>
                        <option value=\"Tim\">Tim, the delivery boy</option>
                        <option value=\"Lisa\">Lisa, the new cashier</option>
                        <option value=\"Mr. Jones\">Mr. Jones, a customer</option>
                    </select>
                    <input type=\"text\" id=\"q4-reason\" class=\"input-text mt-4\" placeholder=\"It was... that...\">
                    <button id=\"submit-q4-btn\" class=\"btn mt-4 w-full\">Submit Answer</button>
                    <p id=\"q4-feedback\" class=\"feedback-message mt-2\"></p>
                </div>
            </div>
            <div id=\"mission-success\" class=\"mission-section hidden text-center\">
                <h2 class=\"text-4xl font-bold text-green-700 mb-4\">Congratulations! Case Solved!</h2>
                <p class=\"text-lg mb-6\">You've unlocked the Cookie Jar of Truth! ...</p>
                <button id=\"restart-btn\" class=\"btn mt-6\">Restart Investigation</button>
            </div>
        </div>
    </div>

    <script>
        const mission_sections = document.querySelectorAll('.mission-section');
        function show_mission(idx){ mission_sections.forEach((m,i)=>{ m.classList.add('hidden'); if(i===idx){ m.classList.remove('hidden'); } }); }
        document.getElementById('start-mission-btn').addEventListener('click', ()=> show_mission(1));
        show_mission(0);

        // 기존 검증 로직 (요약):
        const q1_input = document.getElementById('q1-input');
        const q1_btn = document.getElementById('submit-q1-btn');
        const q1_feedback = document.getElementById('q1-feedback');
        q1_btn.addEventListener('click', ()=>{
            const a = q1_input.value.trim().toLowerCase();
            if(a.includes('it was') && a.includes('the delivery boy') && a.includes('that')){
                q1_feedback.textContent = 'Correct! A clue has been unlocked.';
                q1_feedback.className = 'feedback-message success mt-2';
                setTimeout(()=> show_mission(2), 800);
            } else {
                q1_feedback.textContent = "Incorrect. Remember to start with 'It was... that...' and use the correct suspect.";
                q1_feedback.className = 'feedback-message error mt-2';
            }
        });
        const q2_input = document.getElementById('q2-input');
        const q2_btn = document.getElementById('submit-q2-btn');
        const q2_feedback = document.getElementById('q2-feedback');
        q2_btn.addEventListener('click', ()=>{
            const a = q2_input.value.trim().toLowerCase();
            if(a.includes('it was') && (a.includes('the new cashier') || a.includes('lisa')) && a.includes('that')){
                q2_feedback.textContent = 'Correct! Another clue unlocked.';
                q2_feedback.className = 'feedback-message success mt-2';
                setTimeout(()=> show_mission(3), 800);
            } else {
                q2_feedback.textContent = 'Incorrect. Try again, detective.';
                q2_feedback.className = 'feedback-message error mt-2';
            }
        });
        const q3_input = document.getElementById('q3-input');
        const q3_btn = document.getElementById('submit-q3-btn');
        const q3_feedback = document.getElementById('q3-feedback');
        q3_btn.addEventListener('click', ()=>{
            const a = q3_input.value.trim().toLowerCase();
            const keys = ['behind the counter','cleaning',"couldn't see",'could not see','lying'];
            const ok = keys.some(k=> a.includes(k));
            if(a.includes('lisa') && ok){
                q3_feedback.textContent = "Excellent deduction! You're on the right track.";
                q3_feedback.className = 'feedback-message success mt-2';
                setTimeout(()=> show_mission(4), 800);
            } else {
                q3_feedback.textContent = 'Incorrect. Think about where Lisa said she was standing.';
                q3_feedback.className = 'feedback-message error mt-2';
            }
        });
        const q4_suspect = document.getElementById('q4-suspect');
        const q4_reason = document.getElementById('q4-reason');
        const q4_btn = document.getElementById('submit-q4-btn');
        const q4_feedback = document.getElementById('q4-feedback');
        q4_btn.addEventListener('click', ()=>{
            const suspect = q4_suspect.value;
            const reason = q4_reason.value.trim().toLowerCase();
            const keys = ['lisa','lying','behind the counter',"couldn't see",'could not see','to blame'];
            const ok = keys.some(k=> reason.includes(k));
            if(suspect === 'Lisa' && reason.includes('it was') && reason.includes('that') && ok){
                q4_feedback.textContent = 'Case solved! The cookie thief is Lisa!';
                q4_feedback.className = 'feedback-message success mt-2';
                setTimeout(()=> show_mission(5), 800);
            } else {
                q4_feedback.textContent = 'Incorrect. Re-examine your clues, especially the biggest one!';
                q4_feedback.className = 'feedback-message error mt-2';
            }
        });
        document.getElementById('restart-btn').addEventListener('click', ()=>{ location.reload(); });
    </script>
</body>
</html>"""
    return html_content


def main() -> None:
    """
    Streamlit 앱의 엔트리 포인트입니다.
    - HTML 게임을 임베드하여 동일한 상호작용을 제공합니다.
    """
    st.set_page_config(page_title='The Case of the Missing Cookies', page_icon='🍪', layout='centered')
    st.markdown('## The Case of the Missing Cookies')
    st.caption('Streamlit에서 실행되는 인터랙티브 영어 학습 게임')

    html_content = load_game_html()
    # components_html(html, height)로 렌더링합니다.
    components_html(html_content, height=1200)


if __name__ == '__main__':
    main()

