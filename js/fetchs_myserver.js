// 문의 내용 조회 및 비밀번호 확인 기능 추가
document.querySelectorAll('.content form').forEach(form => {
    form.addEventListener('submit', async event => {
        event.preventDefault(); // 폼 전송을 방지합니다.

        // 필요한 데이터 가져오기
        const inquiryNumber = form.querySelector('[name="inquiryNumber"]').value; // 폼에서 inquiryNumber 값 가져오기
        const passwordInput = form.querySelector('[name="password"]');
        const password = passwordInput.value;

        // 서버에 검증 요청 URL (실제 환경에 맞게 수정 필요)
        let url = `http://127.0.0.1:8000/api/verify_inquiry_password/${inquiryNumber}/${password}`;

        try {
            let response = await fetch(url);
            if (response.ok) {
                let result = await response.json();
                if (result.success) {
                    // 비밀번호가 맞으면 문의 내용 표시
                    form.parentElement.innerHTML = `<p>${result.inquiryContent}</p>`;
                } else {
                    // 비밀번호가 틀리면 오류 메시지 표시
                    alert("비밀번호가 일치하지 않습니다.");
                }
            } else {
                // 응답 오류 처리
                throw new Error('문의사항 검증 실패');
            }
        } catch (error) {
            console.error(`Error: ${error.message}`);
        }
    });
});
