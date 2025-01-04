
from graphql import GraphQLSchema, GraphQLObjectType, GraphQLString, GraphQLField

def create_schema():
    query = GraphQLObjectType(
        name='Query',
        fields={
            'getData': GraphQLField(
                GraphQLString,
                resolve=lambda obj, info: 'Data from GraphQL'
            )
        }
    )
    
    return GraphQLSchema(query=query)
