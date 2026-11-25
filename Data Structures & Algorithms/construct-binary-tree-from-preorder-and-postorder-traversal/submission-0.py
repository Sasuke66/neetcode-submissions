class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> Optional[TreeNode]:
        pass
        def helper(pre,post):
            print('pre is: ', pre, 'post is: ', post)
            if not pre:
                return None
            if len(pre)==1:
                return TreeNode(post.pop())
            node=TreeNode(post.pop())
            ind=pre.index(post[-1])
            node.right=helper(pre[ind:],post)
            node.left=helper(pre[1:ind],post)
            return node
        return helper(pre,post)