#Distribution of Deadline Period DP: dp_d, variable DP: dp_var

dp_d = DiscreteDistribution( {'deadline': 0.25, 'no deadline': 0.75} )

dp_var = Node(dp_d, name ="DP")


#Distribution of Human Intervention HI: hi_d, variable HI: hi_var

hi_d = DiscreteDistribution( {'intervention': 0.15, 'no intervention': 0.85} )

hi_var = Node(hi_d, name ="HI")

#Distribution of Overcrowding O: o_d, variable O: o_var

o_d = ConditionalProbabilityTable( [['deadline', 'crowded', 0.70],
                                   ['deadline', 'not crowded', 0.30],
                                   ['no deadline', 'crowded', 0.10],
                                   ['no deadline', 'not crowded', 0.90]], [dp_var.distribution])

o_var = Node(o_d, name="O")

#Distribution of Manual Control MC: mc_d, variable MC: mc_var

mc_d = ConditionalProbabilityTable( [['crowded','switched', 0.70],
                                   ['crowded', 'untouched', 0.30],
                                   ['not crowded', 'switched', 0.2],
                                   ['not crowded', 'untouched', 0.8]], [o_var.distribution])

mc_var = Node(mc_d, name="MC")


#Distribution of Sensors Activated SA: sa_d, variable SA: sa_var

sa_d = ConditionalProbabilityTable ( [['crowded','intervention','activated',0.95],
                                    ['crowded','intervention','not activated',0.05],
                                    ['crowded','no intervention','activated',0.90],
                                    ['crowded','no intervention','not activated',0.10],
                                    ['not crowded','intervention','activated',0.70],
                                    ['not crowded','intervention','not activated',0.30],
                                    ['not crowded','no intervention','activated',0.05],
                                    ['not crowded','no intervention','not activated',0.95]],
                                    [o_var.distribution, hi_var.distribution])

sa_var = Node(sa_d, name="SA")

#Distribution of Ventilation Activated VA: va_d, variable VA: va_var

va_d = ConditionalProbabilityTable ( [
                                    ['switched','activated','on',0.99],
                                    ['switched','activated','off',0.01],
                                    ['switched','not activated','on',0.90],
                                    ['switched','not activated','off',0.10],
                                    ['untouched','activated','on',0.80],
                                    ['untouched','activated','off',0.20],
                                    ['untouched','not activated','on',0.01],
                                    ['untouched','not activated','off',0.99]],
                                    [mc_var.distribution, sa_var.distribution])

va_var = Node(va_d, name="VA")

#Defining model

model = BayesianNetwork()

model.add_nodes(dp_var, hi_var, o_var, mc_var, sa_var, va_var)

model.add_edge(dp_var, o_var)
model.add_edge(o_var, sa_var)
model.add_edge(o_var, mc_var)
model.add_edge(hi_var, sa_var)
model.add_edge(sa_var, va_var)
model.add_edge(mc_var, va_var)

model.bake()

pred1 = model.predict_proba({'O':'not crowded','MC':'untouched','VA':'on'})

def print_predictions(model, prediction):
    for node, prediction in zip(model.states,prediction):
        if isinstance(prediction, str):
            print(node.name,':',prediction)
        else:
            print(node.name)
            for value, probability in prediction.parameters[0].items():
                print(value,':',probability)

#Scenarios

#Given certain evidences, the BN can be used to predict the most probable scenario, as follows:

obs1a = {'DP': 'no deadline','O': 'crowded','SA': 'not activated'}
obs1b = {'DP': 'no deadline','O': 'crowded','MC': 'untouched'}
obs1c = {'DP': 'no deadline','O': 'crowded','MC': 'untouched','SA': 'not activated'}
model.predict([obs1a,obs1b,obs1c])