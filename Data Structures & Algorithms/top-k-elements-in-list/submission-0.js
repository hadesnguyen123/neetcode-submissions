class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        // duyệt từng phhần tử => mỗi phần tử gán vào trong hash table theo cặp key, value
        let freqMap = new Map()
        for (let num of nums) {
            freqMap.set(num, (freqMap.get(num) || 0) + 1)
        }
        //sắp xếp theo tấn suất giảm dần
        const sorted = [...freqMap.entries()].sort((a, b) => b[1] - a[1]);
        //top K phaanf tuw
        return sorted.slice(0,k).map(entry => entry[0])
    }
}
