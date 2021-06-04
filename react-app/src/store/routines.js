// const SEND_QUESTIONNAIRE = "questionnaire/SEND_QUESTIONNAIRE";

// const sendQuestionnaire = (user) => ({
//     type: SEND_QUESTIONNAIRE,
//     payload: user
// });

export const sendQuestionnaire = (questionnaire) => async (dispatch) => {
    const response = await fetch("/api/questionnaire", {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(questionnaire)
    });
    const data = await response.json();
    if (data.errors) {
        return data;
    }
    // dispatch(removeUser());
    return {}
};