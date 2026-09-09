/**
 * @param {number[][]} graph
 * @return {number[]}
 */
var eventualSafeNodes = function(graph) {
    const _graph = new Graph(graph);
    let nodes = _graph.getNodes().map((val) => parseInt(val) );
    let result = [];
    
    for( let node of nodes ) {
        if( !_graph.hasCycle(node) )
            result.push(node);
    }
    return result;
};


class Graph{
    constructor(edges){
        this._graph = {}
        
        for( let i in edges ) {
            this._graph[i] = edges[i];
        }
    }

    getNodes() {
        return Object.keys(this._graph);
    }

    hasCycle(node) {
        let visited = new Set();
        let visiting = new Set();
        
        return _hasCycle(node, visited, visiting, this._graph);
    }
}


function _hasCycle(node, visited, visiting, graph) { 
    visiting.add(node);
    
    for( let nNode of graph[node] ) {
        if( visiting.has(nNode) )
            return true
        
        if( visited.has(nNode) )
            continue
        
        if( _hasCycle( nNode, visited, visiting, graph ) )
            return true
    }
    
    visiting.delete(node);
    visited.add(node);
    return false;
}