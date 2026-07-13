class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        // const res = {};
        // for (let s of strs) {
        //     const count = new Array(26).fill(0);
        //     for (let c of s) {
        //         count[c.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
        //     }
        //     const key = count.join(',');
        //     if (!res[key]) {
        //         res[key] = [];
        //     }
        //     res[key].push(s);
        // }
        // return Object.values(res);
        

        //should be m*n
        //sort => compare => reuslt => m*nlogn
        const result = {}
        const map = new Map()
        for(let s of strs){
            let shorted = s.split("").sort().join()
            if(!result[shorted]) result[shorted] = []
            result[shorted].push(s)
        }

        return Object.values(result)

    }
}