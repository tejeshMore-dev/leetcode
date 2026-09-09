/**
 * @param {string[]} creators
 * @param {string[]} ids
 * @param {number[]} views
 * @return {string[][]}
 */
var mostPopularCreator = function(creators, ids, views) {
    let map = {};
    let maxTotal = 0;
    
    for( let i=0; i<creators.length; i++ ) {
        let creator = creators[i];
        let id = ids[i];
        let view = views[i];
        
        if( !map[creator] ) {
            map[creator] = {
                total: 0,
                max: 0
            }
            
        }
        
        map[creator].total += view;
        map[creator].max = Math.max(view, map[creator].max);

        if( !map[creator][view])
            map[creator][view] = [];

        map[creator][view].push(id);

        maxTotal = Math.max(maxTotal, map[creator].total);
        
    }
    
    let res = [];
    for( let key in map) {
        if( map[key].total === maxTotal ) {
            let { max } = map[key];
            map[key][max].sort();
            
            res.push([ key, map[key][max][0] ])
        }
    }
    
    return res;
};

/*
 creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4]
map {
    alice :  {
        total: 10
        max : 5
        5: [one, three]
    }
    bob: {
        total:10
        max:10
        10:[two]
    }
}





*/