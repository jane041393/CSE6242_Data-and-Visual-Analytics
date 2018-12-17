package edu.gatech.cse6242;

import org.apache.hadoop.fs.Path;
import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.util.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class Q1 {
	public static class TokenizerMapper extends Mapper<Object, Text, IntWritable, IntWritable>{

		public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
			
			// System.out.print("Before Mapper: " + key + ", " + value);

			String line = value.toString();
			String[] tokens = line.split("\t");
			int source_ID = Integer.parseInt(tokens[0]);
            int target_ID = Integer.parseInt(tokens[1]);
            int weight = Integer.parseInt(tokens[2]);
            context.write(new IntWritable(source_ID), new IntWritable(weight));
            // // System.out.println(
            //         "======" +
            //         "After Mapper:" + new IntWritable(source_ID) + ", " + new IntWritable(weight));
		}
	}

	public static class Reduce_Sum extends Reducer<IntWritable,IntWritable,IntWritable,IntWritable>{
    public void reduce(IntWritable key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException{
      int maxValue = Integer.MIN_VALUE;
      
      for(IntWritable value: values){
        maxValue = Math.max(maxValue, value.get());
      }
      context.write(key, new IntWritable(maxValue));
    }

       		
       }

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "Q1");
     /* TODO: Needs to be implemented */

    job.setJarByClass(Q1.class);
    job.setMapperClass(TokenizerMapper.class);
    job.setCombinerClass(Reduce_Sum.class);
    job.setReducerClass(Reduce_Sum.class);
    job.setOutputKeyClass(IntWritable.class);
    job.setOutputValueClass(IntWritable.class);
   

    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
