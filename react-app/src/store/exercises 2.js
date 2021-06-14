const SET_EXERCISE = 'results/setExercise'

export const setExercise = (exercise) => ({
    type: SET_EXERCISE,
    payload: exercise
})

export const getExcercise = (exersise_id, api_id) => async (dispatch) => {
    const response = await fetch(`/api/exercise/${api_id}`, {
        method: 'GET',
        headers: {
            "Content-Type": "application/json",
        }
    });
    const data = await response.json();
    if (data.errors) {
        return data;
    }
    dispatch(setExercise({ [exersise_id]: data}));
    return {}
};



const initialState = {}

export default function reducer(state=initialState, action) {
    const prevState = state
    switch (action.type) {
        case SET_EXERCISE:
            const newState = {...prevState, ...action.payload}
            return newState
        default:
            return state;
    }
}