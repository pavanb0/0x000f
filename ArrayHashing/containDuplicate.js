var containsDuplicate = function(nums) {
    var out = false;
    nums = nums.sort()
    for (let i=0;i<nums.length;i++){
        if(nums+1<nums){
            if(nums[i]===nums[i+1]){
                out=true;
                break;
            }
        }
    }
    return out
};
console.log(containsDuplicate([1,2,3,1]))