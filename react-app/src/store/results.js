const SET_RESULTS = 'results/setResults'

export const setResults = (result) => ({
    type: SET_RESULTS,
    payload: result
})



const initialState = {}

export default function reducer(state=initialState, action) {
    const prevState = state
    switch (action.type) {
        case SET_RESULTS:
            const newState = {...prevState, ...action.payload}
            return newState
        default:
            return state;
    }
}