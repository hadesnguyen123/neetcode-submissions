class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        //sort. compare => nlogn
        // if(s.length != t.length) 
        //     return false
        // let sSort = s.split("").sort().join();
        // let tSort = t.split("").sort().join();
        // return sSort == tSort

        //Hashmap
        if(s.length != t.length) 
            return false
        let countS = {}
        let countT = {}
        for(let i = 0; i < s.length; i ++){
            countS[s[i]] = (countS[s[i]] || 0) + 1
            countT[t[i]] = (countT[t[i]] || 0) + 1
        }
        for(let key in countS){
            if(countS[key] != countT[key])
                return false
        }

        return true
    }
}
