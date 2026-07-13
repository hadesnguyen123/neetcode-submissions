class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        //Bruth force: 2 for => N2
        //sort?
        //hashmap
        let map = new Map()
        for (let i = 0; i < nums.length; i++) {
            let differ = target - nums[i]
            if (map.has(differ)) {
                return [map.get(differ), i]
            }   //has return key exist
            map.set(nums[i], i)
        }
        return []
    }
}
